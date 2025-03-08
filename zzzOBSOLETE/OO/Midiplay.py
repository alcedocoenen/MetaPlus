import mido

class Midiplay():
    def __init__(self):
        # self.midimessage = midimessage

    def midi_init(self):
        portlist = mido.get_output_names()
        portname = portlist[0]
        port = mido.open_output(portname)
        # FIXME moet nog kijken hoe we dit algemeen kunnen krijgen
        # FIXME foutafhandeling

    def play(self, message):
        # FIXME dit moet nog helemaal kooppend gemaakt worden
        # message is composed as dict
        self.midi_init()
        pitch = message["pitch"]
        velocity = message["velocity"]
        duration = message["duration"]
        channel = message["channel"]
        msg1 = mido.Message('note_on', channel=channel, note = pitch, velocity=velocity, time=duration)
        # Message('note_on', channel=0, note=0, velocity=64, time=0)
        port.send(msg1)
        # FIXME hoe krijgen we nu op tijd een note-off? => nakijken in mido




    def store_in_file(self):
        pass

