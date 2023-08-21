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


# c3_note = Note("data/notes/C3.wav")
# g3_note = Note("data/notes/G3.wav")
# c4_note = Note("data/notes/C4.wav")
# e4_note = Note("data/notes/E4.wav")
# g4_note = Note("data/notes/G4.wav")






# if __name__ == '__main__':

#     c_major_chord = Chord([c3_note, g3_note, c4_note, e4_note, g4_note])
    
#     chord_sound = c_major_chord.create_chord()
#     chord_sound.export("data/chords/chord_c_major.wav", format="wav")

for index, notes in enumerate(all_notes,0):
    print(notes, all_notes[index+4], all_notes[index+4+3])