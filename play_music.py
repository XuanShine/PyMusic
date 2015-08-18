
from music import *
import time

from proba_music import list_to_list_of_music

pitches = "E5, DS5, E5, DS5, E5, B4, D5, C5, A4, REST, C4, E4, A4, B4, REST, E4, GS4, B4, C5, REST, E4, C5, B4, A4".split(", ")
durations = "SN, SN, SN, SN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN".split(", ")

pitches1 = []
for note in list_to_list_of_music(pitches):
    pitches1.append(vars()[note])

durations1 = []
for note in list_to_list_of_music(durations):
    durations1.append(vars()[note])

print(pitches1, durations1)
#theme = Phrase()
#theme.addNoteList(pitches1, durations1)

#Play.midi(theme)
# Algorithmique génétique
