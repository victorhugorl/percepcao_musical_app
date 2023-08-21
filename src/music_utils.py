# aqui vou criar as notas e os acordes para execução do app

from pydub import AudioSegment

all_notes = ('A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab')

class Note:
    def __init__(self, file_path):
        self.sound = AudioSegment.from_wav(file_path)

    def get_sound(self):
        return self.sound
    
class Chord:
    def __init__(self, notes):
        self.notes = notes

    def create_chord(self):
        combined_sound = self.notes[0].get_sound()
        for note in self.notes[1:]:
            combined_sound = combined_sound.overlay(note.get_sound())
        return combined_sound


# tenho que automatizar isso, programador nao fica repetindo codigo
# não sei exatamente como fazer isso, mas penso em closure com loops
# para instanciar essas classes, nao tenho ideia tambem, porque eu teria
# que instanciar todas elas seguindo um padrão cliche

# c3_note = Note("data/notes/C3.wav")
# g3_note = Note("data/notes/G3.wav")
# c4_note = Note("data/notes/C4.wav")
# e4_note = Note("data/notes/E4.wav")
# g4_note = Note("data/notes/G4.wav")

# if __name__ == '__main__':

#     c_major_chord = Chord([c3_note, g3_note, c4_note, e4_note, g4_note])
    
#     chord_sound = c_major_chord.create_chord()
#     chord_sound.export("data/chords/chord_c_major_natural.wav", format="wav")







for index, notes in enumerate(all_notes,0):
    print(notes, all_notes[index+4], all_notes[index+4+3])

# pretendo pensar em uma lógica para criar todos os acordes de uma vez
# tem um padrão ('A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab')
# onde quando chega no último itém, retorna para o primeiro só que uma oitava acima
# no casso tem A0, A1, A2, ...., A7
# preciso criar todos os acordes possiveis, seguindo tônica, quinta, tônica8ª acima,
# terca8ª acima, quinta8ª acima 
# os nomes possuem um padrão: chord_noteThatBegin_majorOrMinor_naturalOrWith9/7/11/13.wav 
# ex:'chord_A0_major_natural.wav' 
# pretendo criar ciclos para criar os acordes maiores naturais, depois os menores,
# e depois as tetrades
# quando a oitava acabar e não der para formar o acorde completo, só não o ter
# *preciso aumentar um pouco o volume de todas as notas e acordes(está muito baixinho)
# 