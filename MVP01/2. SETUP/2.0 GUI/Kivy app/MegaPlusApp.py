# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
import sqlite3
from functools import partial

# Register Noto font
resource_add_path('fonts')
LabelBase.register(name='Noto', fn_regular='NotoSans-Regular.ttf')


class DatabaseManager:
    def __init__(self):
        DATABASE = '/Users/alcedocoenen/Documents/Plus-Minus/Python/MetaPlus/MetaPlus/MVP01/2. SETUP/2.0 GUI/Config_database/configDB'
        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS realisation (
                id INTEGER PRIMARY KEY,
                name TEXT,
                author TEXT,
                version TEXT,
                number_of_layers INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Config_Layer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ref_to_realisation INTEGER,
                layer_id INTEGER,
                name TEXT,
                squarepages TEXT,
                notepages TEXT,
                sequence_offset_start INTEGER,
                sequence_offset_mid INTEGER,
                sequence_offset_end INTEGER,
                staccato_duration INTEGER,
                gracenote_offset INTEGER,
                FOREIGN KEY (realisation_number) REFERENCES realisations(number)
            )
        ''')
        self.conn.commit()


class TitleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        title = Label(
            text='Meta-Plus',
            font_name='Noto',
            font_size='48sp'
        )
        start_button = Button(
            text='Start',
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'center_x': 0.5}
        )
        start_button.bind(on_press=self.switch_to_start)

        layout.add_widget(title)
        layout.add_widget(start_button)
        self.add_widget(layout)

    def switch_to_start(self, instance):
        self.manager.current = 'start'


class StartScreen(Screen):
    def __init__(self, db_manager, **kwargs):
        super().__init__(**kwargs)
        self.db_manager = db_manager

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Tree view for realisations
        self.tree = TreeView(root_options=dict(text='Realisations'),
                             hide_root=False,
                             size_hint_y=0.6)

        # Edit area
        edit_area = GridLayout(cols=2, spacing=5, size_hint_y=0.3)
        self.fields = {}
        for field in ['number', 'name', 'author', 'version', 'number_of_layers']:
            edit_area.add_widget(Label(text=field))
            self.fields[field] = TextInput(multiline=False)
            edit_area.add_widget(self.fields[field])

        # Buttons
        button_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        save_btn = Button(text='Save')
        new_btn = Button(text='New')
        config_btn = Button(text='Config')

        save_btn.bind(on_press=self.save_record)
        new_btn.bind(on_press=self.new_record)
        config_btn.bind(on_press=self.switch_to_config)

        for btn in [save_btn, new_btn, config_btn]:
            button_layout.add_widget(btn)

        layout.add_widget(self.tree)
        layout.add_widget(edit_area)
        layout.add_widget(button_layout)

        self.add_widget(layout)
        self.load_realisations()

    def load_realisations(self):
        self.tree.clear_widgets()
        self.db_manager.cursor.execute('SELECT * FROM realisation')
        for row in self.db_manager.cursor.fetchall():
            node = self.tree.add_node(TreeViewNode(text=f'{row[0]}: {row[1]}'))
            node.bind(on_touch_down=partial(self.load_realisation_details, row))

    def load_realisation_details(self, row, instance, touch):
        if touch.button == 'left':
            for i, field in enumerate(self.fields.keys()):
                self.fields[field].text = str(row[i])

    def save_record(self, instance):
        try:
            values = [self.fields[field].text for field in self.fields.keys()]
            if values[0]:  # Update existing record
                self.db_manager.cursor.execute('''
                    UPDATE realisation 
                    SET name=?, author=?, version=?, number_of_layers=?
                    WHERE id=?
                ''', (values[1], values[2], values[3], int(values[4]), int(values[0])))
            else:  # Insert new record
                self.db_manager.cursor.execute('''
                    INSERT INTO realisation (name, author, version, number_of_layers)
                    VALUES (?, ?, ?, ?)
                ''', (values[1], values[2], values[3], int(values[4])))

            self.db_manager.conn.commit()
            self.load_realisations()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def new_record(self, instance):
        for field in self.fields.values():
            field.text = ''

    def switch_to_config(self, instance):
        if self.fields['number'].text:
            self.manager.get_screen('config').load_configuration(int(self.fields['id'].text))
            self.manager.current = 'config'


class ConfigScreen(Screen):
    def __init__(self, db_manager, **kwargs):
        super().__init__(**kwargs)
        self.db_manager = db_manager
        self.current_realisation = None

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Realisation details area
        self.realisation_info = Label(size_hint_y=0.1)

        # Tree view for configurations
        self.tree = TreeView(root_options=dict(text='Configurations'),
                             hide_root=False,
                             size_hint_y=0.4)

        # Edit area
        edit_area = GridLayout(cols=2, spacing=5, size_hint_y=0.4)
        self.fields = {}
        config_fields = ['layer_id', 'name', 'squarepages', 'notepages',
                         'sequence_offset_start', 'sequence_offset_mid',
                         'sequence_offset_end', 'staccato_duration',
                         'gracenote_offset']

        for field in config_fields:
            edit_area.add_widget(Label(text=field))
            self.fields[field] = TextInput(multiline=False)
            edit_area.add_widget(self.fields[field])

        # Buttons
        button_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        save_btn = Button(text='Save')
        new_btn = Button(text='New')
        back_btn = Button(text='Back')

        save_btn.bind(on_press=self.save_record)
        new_btn.bind(on_press=self.new_record)
        back_btn.bind(on_press=self.switch_to_start)

        for btn in [save_btn, new_btn, back_btn]:
            button_layout.add_widget(btn)

        layout.add_widget(self.realisation_info)
        layout.add_widget(self.tree)
        layout.add_widget(edit_area)
        layout.add_widget(button_layout)

        self.add_widget(layout)

    def load_configuration(self, realisation_number):
        self.current_realisation = realisation_number
        self.db_manager.cursor.execute(
            'SELECT * FROM realisation WHERE id=?',
            (realisation_number,)
        )
        realisation = self.db_manager.cursor.fetchone()
        self.realisation_info.text = f"Realisation: {realisation[1]} (#{realisation[0]})"

        self.tree.clear_widgets()
        self.db_manager.cursor.execute(
            'SELECT * FROM Config_Layer WHERE ref_to_realisation=?',
            (realisation_number,)
        )
        for row in self.db_manager.cursor.fetchall():
            node = self.tree.add_node(TreeViewNode(text=f'Layer {row[2]}: {row[3]}'))
            node.bind(on_touch_down=partial(self.load_configuration_details, row))

    def load_configuration_details(self, row, instance, touch):
        if touch.button == 'left':
            field_values = row[2:]  # Skip id and realisation_number
            for field, value in zip(self.fields.keys(), field_values):
                self.fields[field].text = str(value)

    def save_record(self, instance):
        try:
            values = [self.fields[field].text for field in self.fields.keys()]
            self.db_manager.cursor.execute('''
                INSERT INTO Config_Layer (
                    ref_to_realisation, layer_id, name, squarepages, notepages,
                    sequence_offset_start, sequence_offset_mid, sequence_offset_end,
                    staccato_duration, gracenote_offset
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (self.current_realisation, *values))

            self.db_manager.conn.commit()
            self.load_configuration(self.current_realisation)
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def new_record(self, instance):
        for field in self.fields.values():
            field.text = ''

    def switch_to_start(self, instance):
        self.manager.current = 'start'


class MetaPlusApp(App):
    def build(self):
        self.db_manager = DatabaseManager()

        sm = ScreenManager()
        sm.add_widget(TitleScreen(name='title'))
        sm.add_widget(StartScreen(self.db_manager, name='start'))
        sm.add_widget(ConfigScreen(self.db_manager, name='config'))

        return sm


if __name__ == '__main__':
    MetaPlusApp().run()