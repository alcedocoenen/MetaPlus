# Chords of Notepages

# format of each note = [a,b,c,d]
# a = pitch, b = accent, c = staccato, d = gracenote

import NoteTools as n

# NOTEPAGE 1
chord1 = [[43,0,0,0],[50,0,0,0]]
chord2 = [[39,0,0,0],[45,0,0,0],[50,0,0,0]]
chord3 = [[24,0,0,0],[34,0,0,0],[37,0,0,0],[50,0,0,0]]
chord4 = [[29,0,0,0],[32,0,0,0],[40,0,0,0],[47,0,0,0],[50,0,0,0]]
chord5 = [[25,0,0,0],[30,0,0,0],[39,0,0,0],[43,0,0,0],[48,0,0,0],[50,0,0,0]]
chord6 = [[21,0,0,0],[29,0,0,0],[40,0,0,0],[41,0,0,0],[43,0,0,0],[45,0,0,0],[47,0,0,0],[48,0,0,0],[50,0,0,0]]
chord7 = [[32,0,0,0],[35,0,0,0],[42,0,0,0],[46,0,0,0],[50,0,0,0]]
notepage1 = [chord1,chord2,chord3,chord4,chord5,chord6,chord7]


# NOTEPAGE 2
chord1 = [[97,0,0,0],[102,0,0,0]]
chord2 = [[74,0,0,0],[76,0,0,0],[102,0,0,0]]
chord3 = [[56,0,0,0],[69,0,0,0],[89,0,0,0],[102,0,0,0]]
chord4 = [[47,0,0,0],[52,0,0,0],[60,0,0,0],[94,0,0,0],[102,0,0,0]]
chord5 = [[25,0,0,0],[31,0,0,0],[56,0,0,1],[76,0,0,1],[89,0,0,0],[102,0,0,0]]
chord6_p1 = [[60,0,0,0],[69,0,0,0]]
chord6_p2 = n.make_cluster([83,0,0,0],[102,0,0,0])
chord6 = n.integrate_list([chord6_p1,chord6_p2])
chord7_p1 = n.make_cluster([22,0,0,0],[48,0,0,0])
chord7_p2 = [[87,0,0,1],[91,0,0,0],[102,0,0,0]]
chord7 = n.integrate_list([chord7_p1,chord7_p2])
notepage2 = [chord1,chord2,chord3,chord4,chord5,chord6,chord7]

# NOTEPAGE 3
chord1 = n.make_chord([104,105,107])
chord2 = n.make_chord([94,98,107])
chord3 = n.make_chord([84,87,90,107])
chord4 = n.make_chord([76,77,84,103,107])
chord5 = n.make_chord([80,81,94,99,102,107])
chord6_1 = n.make_chord([86,89])
chord6_2 = n.make_cluster([91,0,0,0],[107,0,0,0])
chord6 = n.integrate_list([chord6_1, chord6_2])
chord7_1 = n.make_cluster([73,0,0,0],[96,0,0,0])
chord7_2 = n.make_chord([100,105,107])
chord7 = n.integrate_list([chord7_1,chord7_2])

notepage3 = [chord1,chord2,chord3,chord4,chord5,chord6,chord7]

# NOTEPAGE 4
chord1 = n.make_chord([79,80])
chord2 = n.make_chord([69,77,80])
chord3 = n.make_chord([64,70,75,80])
chord4 = n.make_chord([54,60,61,74,80])
chord5 = n.make_chord([51,53,67,74,78,80])
chord6_1 = n.make_chord([60,64])
chord6_2 = n.make_cluster([73,0,0,0],[80,0,0,0])
chord6 = n.integrate_list([chord6_1,chord6_2])
chord7_1 = n.make_cluster([70,0,0,0],[57,0,0,0])
chord7_2 = n.make_chord([71,80])
chord7 = n.integrate_list([chord7_1,chord7_2])

notepage4 = [chord1,chord2,chord3,chord4,chord5,chord6,chord7]


# NOTEPAGE 5
chord1 = n.make_chord([84,92,93])
chord2 = n.make_chord([71,82,93])
chord3 = n.make_chord([51,62,80,93])
chord4 = n.make_chord([53,60,64,83,93])
chord5 = n.make_chord([40,54,79,85,89,93])
chord6 = n.make_chord([62,75,90,93])
chord7 = [[46, 1, 0, 1], [60, 0, 0, 0], [61, 0, 0, 0], [62, 0, 0, 0], [63, 0, 0, 0], [64, 0, 0, 0], [65, 0, 0, 0], [66, 0, 0, 0], [67, 0, 0, 0], [92, 0, 0, 0], [93, 0, 0, 0]]


notepage5 = [chord1,chord2,chord3,chord4,chord5,chord6,chord7]


# NOTEPAGE 6
chord1 = [[89,0,0,0],[90,1,0,0],[96,0,0,0]]
chord2 = [[26,0,0,0],[31,0,0,0],[96,0,0,0]]
chord3 = [[37,0,0,0],[40,0,0,0],[80,0,0,0],[96,0,0,0]]
chord4 = [[21,0,0,0],[25,0,0,0],[35,0,0,0],[87,0,0,0],[96,0,0,0]]
chord5 = [[37,0,0,0],[42,0,0,0],[83,0,0,0],[89,0,0,0],[91,0,0,0],[96,0,0,0]]

chord6_p1 = [[28,0,0,0],[39,0,0,0]]
chord6_c1 = n.make_cluster([86,0,0,0],[96,0,0,0])
chord6 = n.integrate_list([chord6_p1,chord6_c1])

chord7_c1 = n.make_cluster([32,0,0,0],[45,0,0,0])
chord7_p2 = [[82,0,0,0],[89,0,0,0],[96,0,0,0]]
chord7 = n.integrate_list([chord7_c1,chord7_p2])

notepage6 = [chord1,chord2,chord3,chord4,chord5,chord6,chord7]



# NOTEPAGE 7
chord1 = [[74,0,0,0],[76,0,0,0]]
chord2 = [[37,0,0,0],[58,0,0,0],[76,0,0,0]]
chord3 = [[45,0,0,0],[56,0,0,0],[65,0,0,0],[76,0,0,0]]
chord4 = [[42,0,0,0],[51,0,0,0],[55,0,0,0],[71,0,0,0],[76,0,0,0]]
chord5 = [[29,0,0,0],[33,0,0,0],[60,0,0,0],[65,0,0,0],[73,0,0,0],[76,0,0,0]]
chord6_p1 = [[22,0,0,0],[31,0,0,0]]
chord6_c1 = n.make_cluster([47,0,0,0],[76,0,0,0])
chord6 = n.integrate_list([chord6_p1,chord6_c1])
chord7 = [[31,0,0,0],[32,0,0,0],[33,0,0,0],[34,0,0,0],[35,0,0,0],[36,0,0,0],[37,0,0,0],[38,0,0,0],[39,0,0,0],[40,0,0,0],[41,0,0,0],[42,0,0,0],[43,0,0,0],[44,0,0,0],[45,0,0,0],[46,0,0,0],[47,0,0,0],[48,0,0,0],[49,0,0,0],[50,0,0,0],[51,0,0,0],[52,0,0,0],[53,0,0,0],[54,0,0,0],[55,0,0,0],[56,0,0,0],[57,0,0,0],[58,0,0,0],[59,0,0,0],[60,0,0,1],[66,0,0,0],[76,0,0,0]]

notepage7 = [chord1,chord2,chord3,chord4,chord5,chord6,chord7]



# all notepages
allchordnotepages = [notepage1, notepage2, notepage3, notepage4, notepage5, notepage6, notepage7]

