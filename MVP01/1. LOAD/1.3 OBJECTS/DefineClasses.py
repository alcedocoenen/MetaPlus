from typing import List, Any

import Configurations as cf
import PlusMinusNotepageChords as pmc
import PlusMinusNotepageSubs as pms


def defineType(klasse):
    return str(type(klasse))[(str(type(klasse)).find("."))+1:-2]

class Square:

    def __init__(self, layerNumber, pageNumber, squareNumber, visibleNumber, boldness, brackets, centralsound, duration, rest, pre_bot, pre_top, mid_bot, mid_top, post_bot, post_top, neben_position, neben_number, neben_speed, flag_top, flag_bottom, coord_timing, coord_pitch, increase, decrease, effect, soundtype):
        self.type = defineType(self)
        # Square id's
        self.LayerNumber = layerNumber
        self.squareNumber = squareNumber
        self.VisibleNumber = visibleNumber
        # references
        self.symbolPageNumber = pageNumber
        # square features
        self.Boldness = boldness
        self.Brackets = brackets
        # Central sound
        self.CentralSound = centralsound
        self.Soundtype = soundtype
        # Accessories
        self.AccessoryPreTop = pre_top
        self.AccessoryPreBottom = pre_bot
        self.AccessoryMidTop = mid_top
        self.AccessoryMidBottom = mid_bot
        self.AccessoryPostTop = post_top
        self.AccessoryPostBottom = post_bot
        # Subsidiary notes
        self.SubsidiariesNumber = neben_number
        self.SubsidiariesSpeed = neben_speed
        self.SubsidiariesPosition = neben_position
        # Effect and duration
        self.Effect = effect
        self.Rest = rest
        self.Duration = duration
        # Tendency
        self.Increase = increase
        self.Decrease = decrease
        # Flags
        self.FlagTop = flag_top
        self.FlagBottom = flag_bottom
        # coordination
        self.CoordinationTiming = coord_timing
        self.CoordinationPitch = coord_pitch

        # connection with notepages

        self.NotePageNumber = self.get_note_page_nr()
        self.Chord_nr = self.Soundtype  # should be the same as the Soundtype
        self.Sequence = []
        # choices
        self.Change_possibilities = []
        self.Original_change_direction = []
        self.Combi_Effect = []


    def print_square(self):
        print(f"\n Square nr {self.squareNumber} of Symbolpage nr {self.symbolPageNumber}")
        print(f"Layernumber: {self.LayerNumber}")
        print(f"Boldness: {self.Boldness}")
        print(f"Brackets: {self.Brackets}")
        print(f"Central sound: {self.CentralSound}")
        print(f"Accessory PreTop: {self.AccessoryPreTop}")
        print(f"Accessory PreBottom: {self.AccessoryPreBottom}")
        print(f"Accessory MidTop: {self.AccessoryMidTop}")
        print(f"Accessory MidBottom: {self.AccessoryMidBottom}")
        print(f"Accessory PostTop: {self.AccessoryPostTop}")
        print(f"Accessory PostBottom: {self.AccessoryPostBottom}")
        print(f"SubsidiariesNumber: {self.SubsidiariesNumber}")
        print(f"SubsidiariesSpeed: {self.SubsidiariesSpeed}")
        print(f"SubsidiariesPosition: {self.SubsidiariesPosition}")
        print(f"Effect: {self.Effect}")
        print(f"Rest: {self.Rest}")
        print(f"Duration: {self.Duration}")
        print(f"Increase: {self.Increase}")
        print(f"Decrease: {self.Decrease}")
        print(f"FlagTop: {self.FlagTop}")
        print(f"FlagBottom: {self.FlagBottom}")
        print(f"CoordinationTiming: {self.CoordinationTiming}")
        print(f"CoordinationPitch: {self.CoordinationPitch}")
        print(f"Soundtype: {self.Soundtype}")
        print(f"Type: {self.type}")
        print(f"NotePageNumber: {self.NotePageNumber}")
        print(f"Chord_nr: {self.Chord_nr}")
        print(f"Sequence: {self.Sequence}")
        print(f"Change_possibilities: {self.Change_possibilities}")
        print(f"Original_change_direction: {self.Original_change_direction}")


    def make_sequence(self):
        # define self.sequence list
        # convert notes to playable midi values
        # original notes format: [a,b,c,d] => a = pitch, b = accent, c = staccato, d = gracenote
        # target note format: [a,b,c,d] => a = pitch, b = volume, c = duration, d = timepoint

        # make sequence based on accidents, centralsound and subs
        # sequence 1 = accidents
        # sequence 2 = centralsound
        # sequence 3 = subs

        # per sequence needs to specify:
        # sequence of pitches
        # sequences of volumes
        # sequence of durations
        # sequence of timepoints

        # timepoints convention used for this app:
        # each square gets 99 timepoints
        # 0 = start of square (accidents pre-)
        # 33 = middle of square (central sound)
        # 66 = third part of square (accidents post)
        # 99 = end timepoint

        total_sequence = []
        seq_acc = self.make_sequence_acc()
        seq_cs = self.make_sequence_cs()
        seq_subs = self.make_sequence_subs()

        total_sequence = [seq_acc, seq_cs, seq_subs]
        return total_sequence


    
    def make_sequence_acc(self):

        # accidents duration
        # short = duration of 10 timepoints
        # medium = duration of 20 timepoints
        # long = duration of 30 timepoints

        # accidents pitch
        # needs to be defined centrally
        # here first a default value of ??

        sequence_acc = []

        # een sequence bestaat  per definitie alleen maar uit een list van notes van formaat [a,b,c,d,e]
        # waarbij a = pitch, b = timepoint, c = duration, d = velocity, en e = channel.

        # pitch for accidents:
        # short pitch = 60
        # medium pitch = 61
        # long pitch = 62

        result1 = []
        result2 = []
        result3 = []

        acc_offset_start = cf.get_offset_sequence("start")
        acc_offset_mid = cf.get_offset_sequence("mid")
        acc_offset_end = cf.get_offset_sequence("end")

        acc_channel = cf.get_accident_channel()
        acc_duration = cf.get_default_accident_duration()
        acc_velocity = cf.get_default_accident_volume()

        accB = self.AccessoryPreBottom
        accT = self.AccessoryPreTop
        result1 = self.process_accidents(accB, accT, acc_offset_start, acc_channel, acc_duration, acc_velocity)

        accB = self.AccessoryMidBottom
        accT = self.AccessoryMidTop
        result2 = self.process_accidents(accB, accT, acc_offset_mid, acc_channel, acc_duration, acc_velocity)


        accB = self.AccessoryPostBottom
        accT = self.AccessoryPostTop
        result3 = self.process_accidents(accB, accT, acc_offset_end, acc_channel, acc_duration, acc_velocity)


        for el in result1:
            if type(el) is type([]):
                sequence_acc.append(el)
        for el in result2:
            if type(el) is type([]):
                sequence_acc.append(el)
        for el in result3:
            if type(el) is type([]):
                sequence_acc.append(el)

        return sequence_acc

    def process_accidents(self, accB, accT, offset, channel=9, acc_duration = 1, acc_velocity = 100):
        # if one or both of pre-accidents is not 0, then rhythm starts with 0
        # for both top and bottom: if pre-acc is not 0, then melody is 60, duration is according to value of accident
        # if one or both of mid-accidents is not 0, then next rhythm value is 33 + next melody is 60
        # if one or both of post-accidents is not 0, then next rhythm value is 66 + next melody is 60

        acc_short_pitch = cf.get_accident_pitch("short")
        acc_medium_pitch = cf.get_accident_pitch("medium")
        acc_long_pitch = cf.get_accident_pitch("long")

        temp_melody = []
        # temp_note = []
        if (accB != 0) or (accT != 0):
            if (accB > 0):
                if (accB == 1):
                    temp_note = [acc_short_pitch, offset, acc_duration, acc_velocity, channel]
                    temp_melody.append(temp_note)
                elif (accB == 2):
                    temp_note = [acc_medium_pitch, offset, acc_duration, acc_velocity, channel]
                    temp_melody.append(temp_note)
                elif (accB == 3):
                    temp_note = [acc_long_pitch, offset, acc_duration, acc_velocity, channel]
                    temp_melody.append(temp_note)
            if (accT > 0):
                if (accT == 1):
                    temp_note = [acc_short_pitch, offset, acc_duration, acc_velocity, channel]
                    temp_melody.append(temp_note)
                elif (accT == 2):
                    temp_note = [acc_medium_pitch, offset, acc_duration, acc_velocity, channel]
                    temp_melody.append(temp_note)
                elif (accT == 3):
                    temp_note = [acc_long_pitch, offset, acc_duration, acc_velocity, channel]
                    temp_melody.append(temp_note)

            # noten worden gebouwd van formaat [a,b,c,d,e]
            # waarbij a = pitch, b = timepoint, c = duration, d = velocity, en e = channel.

        return temp_melody


    def make_sequence_cs(self):
        sequence_cs = []

        offset = cf.get_default_cs_offset()
        channel = cf.get_default_cs_channel()

        # get_chord_notes
        notepagenr = self.get_note_page_nr()
        chordnr = self.Soundtype
        sequence_cs = self.get_chord_notes(notepagenr, chordnr, offset, channel)
        return sequence_cs

    def make_sequence_subs(self):
        sequence_subs = []
        notepagenr = self.NotePageNumber
        subsnr = self.SubsidiariesNumber
        # get_subs_notes
        subspos = self.SubsidiariesPosition
        if subspos == 0:
            # subspos 0 mens there is no subsidiary notegroup defined, the list should remain empty
            sequence_subs = []
        else:
            if subspos == 1:
                offset = cf.get_offset_sequence("start")
            elif subspos == 2:
                offset = cf.get_offset_sequence("mid")
            elif subspos == 3:
                offset = cf.get_offset_sequence("end")
            else:
                offset = 0
            channel = cf.get_default_subs_channel()
            sequence_subs = self.get_subs_notes(notepagenr, subsnr, offset, channel)

        return sequence_subs

    def get_note_page(self):
        # get the note page
        # return page
         pass

    def get_note_page_nr(self):
        # get the note page number
        # return page number
        config = cf.get_config1()
        layerconfig = config[self.LayerNumber]
        order_notepages = layerconfig["order of notepages"]
        order_squarepages = layerconfig["order of squarepages"]
        this_square_page = self.symbolPageNumber
        indexnr = order_squarepages.index(this_square_page)
        this_note_page_nr = order_notepages[indexnr]
        return this_note_page_nr

    def get_chord_notes(self, NotePageNumber, Chord_nr, offset, channel):
        # get the chord notes
        # return chord
        # bij wijze van test een Chord van een Notepage


        notepage = pmc.allchordnotepages[NotePageNumber-1]
        original_chord = notepage[Chord_nr-1]
        #print(original_chord)
        # sample original_chord = [[45, 1, 0, 0], [56, 0, 1, 0], [65, 0, 0, 0], [76, 0, 0, 1]]
        # format: [a,b,c,d] => a = pitch, b = accent, c = staccato, d = gracenote
        # convert to [a,b,c,d,e] => a = pitch, b = timepoint, c = duration, d = velocity, en e = channel.

        chord = []
        for note in original_chord:

            temp_note = self.make_note(note, offset, channel,"cs")
            chord.append(temp_note)

        return chord

    def make_note(self, note, offset, channel, sequence_type):
        default_volume = cf.get_default_volume(sequence_type)
        default_duration = cf.get_default_duration(sequence_type)

        pitch = note[0]

        if note[1] == 1:  # accent
            velocity = default_volume + cf.get_accent_addition()
        else:
            velocity = default_volume

        if note[2] == 1:  # staccato
            duration = cf.get_staccatao_duration(default_duration)
        else:
            duration = default_duration

        if note[3] == 1:  # gracenote
            timepoint = offset + cf.get_gracenote_offset()
        else:
            timepoint = offset

        midi_note = [pitch, timepoint, duration, velocity, channel]
        return midi_note

    def make_tremolo(self, notes, offset, channel, sequence_type):
        tremolo = []
        # make a tremolo based on the list of (two) notes
        # tremolo should be a list of notes of format [a,b,c,d,e]

        default_volume = cf.get_default_volume(sequence_type)
        default_duration = cf.get_default_duration(sequence_type)
        default_shortest_duration = 0.1;
        # assumed shortest time for a single note in a tremolo is 0.1
        # the number of repetitions is then default_duration / shortest_duration

        tremolo_repetitions: int = default_duration / default_shortest_duration

        switch = False
        for i in range(tremolo_repetitions):
            if switch:
                note = notes[0]
            else:
                note = notes[1]
            switch = not (switch)
            temp_note = self.make_note(note, offset, channel, sequence_type)
            offset = offset + default_shortest_duration
            tremolo.append(temp_note)
        return tremolo

    def get_subs_notes(self, NotePageNumber, SubsidiariesNumber, offset, channel):
        melody = []
        notepage = pms.allsubsnotepages[NotePageNumber-1]
        original_subs = notepage[SubsidiariesNumber - 1]
        default_timepoint_distance = cf. get_default_subs_timepoint_distance()
        #print(original_subs)

        # format: [a,b,c,d] => a = pitch, b = accent, c = staccato, d = gracenote
        # TODO when b = 2 => tremolo
        # convert to [a,b,c,d,e] => a = pitch, b = timepoint, c = duration, d = velocity, en e = channel.

        subnotes = original_subs
        timepoint = offset
        for group in subnotes:
            # first check if it is a chord (a list of lists) or just one note
            if type(group[0]) == type(5):
                # it is not a chord!
                note = group
                midi_note = self.make_note(note, timepoint, channel, "subs")
                melody.append(midi_note)
                timepoint = timepoint + default_timepoint_distance
            else:
                # it is a chord
                tremolo_counter = 0
                tremolo = []
                midi_notes: []
                for note in group:
                    if note[1] == 2:  # it is a tremolo
                        tremolo_counter = tremolo_counter + 1
                        tremolo.append(note)
                        if tremolo_counter > 1: # assumed that tremolos only occur with 2 notes
                            midi_notes = self.make_tremolo(tremolo, timepoint, channel, "subs")
                            # midi_notes is a list of notes in the target format [a,b,c,d,e]
                            for tremolo_note in midi_notes:
                                melody.append(tremolo_note)
                            tremolo_counter = 0
                            tremolo = []
                    else: # it is not a tremolo
                        midi_note = self.make_note(note, timepoint, channel, "subs")
                        melody.append(midi_note)
                timepoint = timepoint + default_timepoint_distance

        return melody

    def play_sequence(self, sequence):
        # play the sequence
        # simulate first with printing
        # return print("ready")
        pass

    # SERIES OF SET and RESET FUNCTIONS TO MANIPULATE THE SETTINGS OF THE SQUARE
    def set_notepagenr(self, nr):
        self.NotePageNumber = nr
        pass

    def reset_notepagenr(self):
        self.NotePageNumber = self.get_note_page_nr()
        pass






# bij wijze van test een hele Square
# neem square 40 van symbolpage 1
# 1, 1,42,40,0,0,6,0,3,2,0,2,0,2,0,1,6,8,0,0,6,0,0,3,1,7
# pas op: layernr toegevoegd als 1e nummer
# square1_40 = Square(1, 1,42,40,0,0,6,0,3,2,0,2,0,2,0,1,6,8,0,0,6,0,0,3,1,7)
square1_40 = Square(1, 1,42,40,0,0,6,0,3,0,0,2,0,2,3,1,6,8,0,0,6,0,0,3,1,7)

square1_40.print_square()
square1_40.set_notepagenr(1)

seq = square1_40.make_sequence()
print(f" accidents: {seq[0]}")
print(f" central sound: {seq[1]}")
print(f" subsidiaries {seq[2]}")

#print(seq)

'''
for element in seq:
    if type(element) is type([]):
        for el in element:
            print(el)
    else:
        print(element)
'''

# om de sequence te bepalen, moet
# 1. eerst de configuratie worden opgehaald om de matchende notepage te vinden. Import Configurations.py, functie get_config1()
# 2. de notepage moet worden opgehaald, aan de hand van de symbolpage
# 3. de notepage moet worden geparsed om de chord en melody te bepalen

