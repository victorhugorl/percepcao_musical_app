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
    
c_note = Note("../data/notes/C3.wav")
e_note = Note("../data/notes/E3.wav")
g_note = Note("../data/notes/G3.wav")

c_major_chord = Chord([c_note, e_note, g_note])
chord_sound = c_major_chord.create_chord()
chord_sound.export("../data/chords/chord_c_major.wav", format="wav")