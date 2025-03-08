from OO import OO_Score as o

# Square test


# Notegroup test

NotePageRecord = []



noteslist01 = []
Note01 = o.Note(74, 100, 0, 0, 0)
Note02 = o.Note(76, 100, 0, 0, 0)
noteslist01.append(Note01)
noteslist01.append(Note02)
Chord01 = o.Chord(1,noteslist01)


noteslist02 = []
Note03 = o.Note(37, 100, 0, 0, 0)
Note04 = o.Note(58, 100, 0, 0, 0)
Note05 = o.Note(76, 100, 0, 0, 0)
noteslist02.append(Note03)
noteslist02.append(Note04)
noteslist02.append(Note05)
Chord02 = o.Chord(1,noteslist02)



Mng01 = o.MainNoteGroup(1, 1, Chord01) # notepage 1, chord 1
Mng02 = o.MainNoteGroup(1, 2, Chord02) # notepage 2, chord 2


print(Note01.makeJson())
Note03.play()
Note04.play()
Note05.play()

# Subsnotegroup test
