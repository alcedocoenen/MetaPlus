
from midiutil import MIDIFile

# ===== DATA =========
#melody = [[76, 31], [81, 22], [74, 56], 97, 60, 47, 76, 78]  # MIDI note number
melody1 = [76, [81,60], 74, 97, 47]
rhythm1 = [0,1,3,4,6]
velocity1 = [60,120,60,120,50]

melody2 = [78, 60, 31, 104, 107, 109]
rhythm2 = [0,1,2,3,4,5]
velocity2 = [100,100,100,100,100,100]

sequence1 = [melody1, rhythm1, velocity1]
sequence2 = [melody2, rhythm2, velocity2]

# piece = [melody1, melody2]

# melody  = [76, 81, [74,56], 97, 60, 47, 76, 78]  # MIDI note number


# ======= FUNCTIONS ============

def setup_MidiFile():

    track = 0
    channel = 0
    time = 0  # In beats
    duration = 1  # In beats
    tempo = 180  # In BPM
    volume = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, time, tempo)

    return MyMIDI

def make_midi_sequence (sequence, Midi_file, track=0, channel=0, duration=1):
    melody = sequence[0]
    rhythm = sequence[1]
    velocity = sequence[2]

    for i, pitch in enumerate(melody):
        # print(i, pitch, type(pitch))
        timepoint = rhythm[i]
        volume = velocity[i]
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
MyMIDI = setup_MidiFile()
MIDI1 = make_midi_sequence(sequence2, MyMIDI, 0, 0, 1)
MIDI2 = make_midi_sequence(sequence1, MyMIDI, 0, 0, 1)
write_midi(MyMIDI,"output2.mid")







