
from midiutil import MIDIFile

channel = 0

# ===== DATA =========
#melody = [[76, 31], [81, 22], [74, 56], 97, 60, 47, 76, 78]  # MIDI note number
melody1 = [76, [81,60], 74, 97, 47]
rhythm1 = [0,1.5,3,4,6]
duration1 = [1,2,1,2,1]
velocity1 = [60,120,60,120,50]
channel1 = [0,0,0,0,0]

melody2 = [78, 60, 31, 104, 107, 109]
rhythm2 = [0,1,2,3,4,5]
duration2 = [2,2,2,4,2,2]
velocity2 = [100,100,100,100,100,100]
channel2 = [9,9,9,9,9,9]

melody3 = [60, 61, 62, 63, 64, 65]
rhythm3 = [0,1,2,3,4,5]
duration3 = [1,1,1,1,1,1]
velocity3 = [100,100,100,100,100,100]
channel3 = [9,9,9,9,9,9]

sequence1 = [melody1, rhythm1, duration1, velocity1, channel1]
sequence2 = [melody2, rhythm2, duration2, velocity2, channel2]
sequence3 = [melody3, rhythm3, duration3, velocity3, channel3]

# piece = [melody1, melody2]

# melody  = [76, 81, [74,56], 97, 60, 47, 76, 78]  # MIDI note number

# ======= FUNCTIONS ============

def convert_note_sequence_to_midi_sequences(note_sequence):
    # note_sequence is a list existing of notes
    # each note is a list [a,b,c,d,e] => a = pitch, b = timepoint, c = duration, d = velocity, en e = channel.
    midi_pitch_sequence = []
    midi_timepoint_sequence = []
    midi_duration_sequence = []
    midi_volume_sequence = []
    midi_channel_sequence = []

    for note in note_sequence:
        midi_pitch_sequence.append(note[0])
        midi_timepoint_sequence.append(note[1])
        midi_duration_sequence.append(note[2])
        midi_volume_sequence.append(note[3])
        midi_channel_sequence.append(note[4])

    return [midi_pitch_sequence, midi_timepoint_sequence, midi_duration_sequence, midi_volume_sequence, midi_channel_sequence]

def do_change(mymidi, channel, program):
    track = 0
    # channel = 0
    time = 0  # Eight beats into the composition
    # program = 42  # A Cello
    mymidi.addProgramChange(track, channel, time, program)

def setup_MidiFile():

    track = 0
    # channel = channel
    time = 0  # In beats
    tempo = 180  # In BPM
    # volume = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(3)  # One track, defaults to format 1 (tempo track is created automatically)
    track = 0
    # channel = channel
    time = 0  # In beats
    tempo = 180  # In BPM
    # volume = 100  # 0-127, as per the MIDI standard
    MyMIDI.addTempo(track, time, tempo)

    track = 1
    # channel = channel
    time = 0  # In beats
    tempo = 180  # In BPM
    # volume = 100  # 0-127, as per the MIDI standard
    MyMIDI.addTempo(track, time, tempo)

    track = 2
    # channel = channel
    time = 0  # In beats
    tempo = 180  # In BPM
    # volume = 100  # 0-127, as per the MIDI standard
    MyMIDI.addTempo(track, time, tempo)

    return MyMIDI

def make_midi_sequence (sequence, Midi_file, track, channel):
    melody = sequence[0]
    rhythm = sequence[1]
    dur = sequence[2]
    velocity = sequence[3]
    chan = sequence[4]


    for i, pitch in enumerate(melody):
        # print(i, pitch, type(pitch))
        timepoint = rhythm[i]
        volume = velocity[i]
        duration = dur[i]
        channel = chan[i]
        if type(pitch) is int:
            # print(track,channel,pitch,timepoint,duration,volume)
            Midi_file.addNote(track, channel, pitch, timepoint, duration, volume)
        elif type(pitch) is list:
            for j, note in enumerate(pitch):
                Midi_file.addNote(track, channel, note, timepoint, duration, volume)
    return Midi_file

def write_midi (midisequence, outputname):
    with open(outputname, "wb") as output_file:
        midisequence.writeFile(output_file)


# ======= EXECUTION ============
# execute

#test cases
accidents = [[61, 4, 1, 100, 9], [61, 8, 1, 100, 9], [62, 8, 1, 100, 9]]
central_sounds = [[73, 4, 2, 100, 1], [74, 4, 2, 100, 1], [75, 4, 2, 100, 1], [76, 4, 2, 100, 1], [77, 4, 2, 100, 1], [78, 4, 2, 100, 1], [79, 4, 2, 100, 1], [80, 4, 2, 100, 1], [81, 4, 2, 100, 1], [82, 4, 2, 100, 1], [83, 4, 2, 100, 1], [84, 4, 2, 100, 1], [85, 4, 2, 100, 1], [86, 4, 2, 100, 1], [87, 4, 2, 100, 1], [88, 4, 2, 100, 1], [89, 4, 2, 100, 1], [90, 4, 2, 100, 1], [91, 4, 2, 100, 1], [92, 4, 2, 100, 1], [93, 4, 2, 100, 1], [94, 4, 2, 100, 1], [95, 4, 2, 100, 1], [96, 4, 2, 100, 1], [100, 4, 2, 100, 1], [105, 4, 2, 100, 1], [107, 4, 2, 100, 1]]
#subsidiaries = [[56, 0, 2, 100, 2], [89, 0, 2, 100, 2], [69, 0.1, 2, 100, 2], [97, 0.1, 2, 100, 2], [102, 0.2, 2, 100, 2], [24, 0.3, 2, 100, 2], [31, 0.3, 2, 100, 2], [83, 4, 2, 100, 2], [94, 4, 2, 100, 2], [74, 5, 2, 100, 2], [76, 5, 2, 100, 2], [87, 6, 2, 100, 2], [89, 6, 2, 100, 2], [49, 7, 2, 100, 2], [56, 7, 2, 100, 2], [69, 8, 2, 100, 2], [102, 8, 2, 100, 2], [60, 9, 2, 100, 2], [89, 9, 2, 100, 2], [74, 10, 2, 100, 2], [97, 10, 2, 100, 2], [56, 11, 2, 100, 2], [94, 11, 2, 100, 2], [67, 12, 2, 100, 2], [69, 12, 2, 100, 2]]
subsidiaries = [[56, 0, 0.5, 100, 2], [89, 0, 0.5, 100, 2], [69, 0.3, 0.5, 100, 2], [97, 0.3, 0.5, 100, 2], [102, 0.6, 0.5, 100, 2], [24, 0.8999999999999999, 0.5, 100, 2], [31, 0.8999999999999999, 0.5, 100, 2], [83, 1.2, 0.5, 100, 2], [94, 1.2, 0.5, 100, 2], [74, 1.5, 0.5, 100, 2], [76, 1.5, 0.5, 100, 2], [87, 1.8, 0.5, 100, 2], [89, 1.8, 0.5, 100, 2], [49, 2.1, 0.5, 100, 2], [56, 2.1, 0.5, 100, 2], [69, 2.4, 0.5, 100, 2], [102, 2.4, 0.5, 100, 2], [60, 2.6999999999999997, 0.5, 100, 2], [89, 2.6999999999999997, 0.5, 100, 2], [74, 2.9999999999999996, 0.5, 100, 2], [97, 2.9999999999999996, 0.5, 100, 2], [56, 3.2999999999999994, 0.5, 100, 2], [94, 3.2999999999999994, 0.5, 100, 2], [67, 3.599999999999999, 0.5, 100, 2], [69, 3.599999999999999, 0.5, 100, 2]]

acc_sequences = convert_note_sequence_to_midi_sequences(accidents)
cs_sequences = convert_note_sequence_to_midi_sequences(central_sounds)
subs_sequences = convert_note_sequence_to_midi_sequences(subsidiaries)



MyMIDI = setup_MidiFile()

#MIDI1 = make_midi_sequence(sequence1, MyMIDI, 0, channel)
#MIDI2 = make_midi_sequence(sequence2, MyMIDI, 1, channel)
#MIDI3 = make_midi_sequence(sequence3, MyMIDI, 0, channel)

MIDI4 = make_midi_sequence(acc_sequences, MyMIDI, 0, 9)
MIDI5 = make_midi_sequence(cs_sequences, MyMIDI, 1, 1)
MIDI6 = make_midi_sequence(subs_sequences, MyMIDI, 2, 1)

# do_change(MyMIDI, 0, 1)
# do_change(MyMIDI, 8, 42)
write_midi(MyMIDI,"output.mid")







