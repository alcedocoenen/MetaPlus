from pony.orm import *


db = Database()


class Realisation(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    author = Optional(str)
    version = Optional(str)
    config__layers = Set('Config_Layer')
    number_of_layers = Optional(int)


class Config_Layer(db.Entity):
    layer_id = PrimaryKey(int, auto=True)
    name = Optional(str)
    squarepages = Optional(str)
    notepages = Optional(str)
    ref_to_realisation = Required(Realisation)
    sequence_offset_start = Optional(int)
    sequence_offset_mid = Optional(int)
    sequence_offset_end = Optional(int)
    staccato_duration = Optional(int)
    gracenote_offset = Optional(int)
    cs_instrument = Optional(str)
    cs_midi_channel = Optional(int)
    cs_midi_instrument = Optional(int)
    cs_def_volume = Optional(int)
    cs_def_duration = Optional(int)
    acc_instrument = Optional(str)
    acc_midi_channel = Optional(int)
    acc_midi_instrument = Optional(int)
    acc_def_volume = Optional(int)
    acc_def_duration = Optional(int)
    acc_pitch_short = Optional(int)
    acc_pitch_medium = Optional(int)
    acc_pitch_long = Optional(int)
    subs_instrument = Optional(str)
    subs_midi_channel = Optional(int)
    subs_midi_instrument = Optional(int)
    subs_def_volume = Optional(int)
    subs_def_duration = Optional(int)
    subs_timepoint_distance = Optional(int)
    config__pages = Set('Config_Page')


class Config_Page(db.Entity):
    page_id = PrimaryKey(int, auto=True)
    page_nr = Required(int)
    ref_to_layer = Required(Config_Layer)
    config__squares = Set('Config_Square')


class Config_Square(db.Entity):
    square_id = PrimaryKey(int, auto=True)
    square_nr = Required(int)
    preferred_changedir = Optional(int)
    replaced_changevalue = Optional(int)
    ref_to_page = Required(Config_Page)



db.generate_mapping()