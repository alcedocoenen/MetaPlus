# some basic functions
def make_cluster(start,end):
    if start > end: # switch when not in right order
        start = end
        end = start
    if isinstance(start,int):
        start = [start,0,0,0]
        end = [end,0,0,0]
    cluster_list = []
    amount_of_notes = end[0] - start[0] + 1
    accent = start[1]
    stacc = start[2]
    grace = start[3]
    newnotes = []
    next_nr = start[0]
    for nr in range(amount_of_notes):
        newnotes.append(next_nr)
        next_nr = next_nr + 1
    for note in newnotes:
        newnotecomplete = [note,accent,stacc,grace]
        cluster_list.append(newnotecomplete)
    return cluster_list

def integrate_list(structured_list):
    new_list = []
    for l in structured_list:
        for element in l:
            new_list.append(element)
    return new_list

def make_chord(list_of_pitches):
    result = []
    for pitch in list_of_pitches:
        note = [pitch,0,0,0]
        result.append(note)
    return result
