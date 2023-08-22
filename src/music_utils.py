# aqui vou criar as notas e os acordes para execução do app

from pydub import AudioSegment

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

def create_note_instances(base_note, octave_range):
    notes = []
    for octave in octave_range:
        note_instance = None
        note_file = f"data/notes/{base_note}{octave}.wav"
        
        try:
            note_instance = Note(note_file)
        except FileNotFoundError:
            print(f'{note_file} nao encontrado') 
            pass
        notes.append(note_instance)
    return notes

def create_chord_instance(base_note, chord_type, modifier, octave_range):
    chord_name = f"chord_{base_note}{octave_range[0]}_{chord_type}_{modifier}.wav"
    chord_notes = create_note_instances(base_note, octave_range)
    chord = Chord(chord_notes)
    chord_sound = chord.create_chord()
    chord_sound.export(f"data/chords/{chord_name}", format="wav")

# all_notes = ('A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab')
# octaves_chords = (('0','1'),('1','2'),('2','3'),('3','4'),('4','5'),('5','6'),('6','7'))
all_notes = ('A','Bb')
octaves_chords = (('0','1'),('1','2'))

for octaves in octaves_chords:
    for note in all_notes:
        create_note_instances(note, octaves)
        base_note = f'{note}{octaves[0]}'
        create_chord_instance(base_note,'major','natural',octaves)
        








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

#    
    
#     chord_sound = c_major_chord.create_chord()
#     chord_sound.export("data/chords/chord_c_major_natural.wav", format="wav")








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