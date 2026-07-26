from music import *

tempo = 120
"""
HN -> BLANCA
QN -> NEGRA
DQN -> NEGRA CON PUNTO
EN -> CORCHEA
WN  -> REDONDA
DHN -> BLANCA CON PUNTO
"""

notes = [


    (G3, EN),
    (B3, EN),
    (D4, EN),
    (B3, QN),
    (FS4, QN),

    (FS4, EN),
    (E4, EN),
    (D4, QN),
    (D4, EN),
    (E3, DQN),
    (REST, EN),

    (E3, EN),
    (G3, EN),
    (B3, EN),
    (D4, EN),
    (B3, QN),
    (FS4, QN),


    (FS4, EN),
    (E4, EN),
    (D4, QN),
    (D4, EN),
    (E3, DQN),

]


primeraVuelta = [
    (REST, QN),
    (E3, DQN),

] + notes

segundaVuelta = [
    (E3, DQN),
] + notes


notas = primeraVuelta + segundaVuelta



def playNotes(notas, tempo):
    frase = Phrase()

    for tono, duracion in notas:
        nota = Note(tono, duracion)
        frase.addNote(nota)

    Mod.tiePitches(frase)

    frase.setTempo(tempo)

    return frase


frase = playNotes(notas, tempo)
frase.setInstrument(VIBRAPHONE)

Play.midi(frase)
Write.midi(frase, "AAngela_Garcia_melodia3.mid")
print("Se creo .mid")