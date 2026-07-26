from music import *

tempo = 120
"""
HN -> BLANCA
QN -> NEGRA
DQN -> NEGRA CON PUNTO
EN -> CORCHEA
"""

notas = [
    (REST, QN),
    (A4, EN),
    (F4, EN),
    (G4, EN),
    (A4, QN),
    (F4, EN),

    (F4, QN),
    (A4, EN),
    (F4, EN),
    (G4, EN),
    (A4, DQN),

    (REST, QN),
    (A4, EN),
    (F4, EN),
    (G4, EN),
    (A4, QN),
    (F4, EN),

    (F4, QN),
    (C4, EN),
    (A4, EN),
    (G4, EN),
    (F4, DQN)
]


def playNotes(notas, tempo):
    frase = Phrase()

    for tono, duracion in notas:
        nota = Note(tono, duracion)
        frase.addNote(nota)

    Mod.tiePitches(frase)

    frase.setTempo(tempo)

    return frase


frase = playNotes(notas, tempo)
frase.setInstrument(MARIMBA)

Play.midi(frase)
Write.midi(frase, "AAngela_Garcia_melodia2.mid")
print("Se creo .mid")