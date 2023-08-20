import fluidsynth
import mido

def play_note():
    # Carregue o SoundFont
    fs = fluidsynth.Synth()
    fs.start(driver="dsound")  # Use o driver apropriado para o seu sistema (ex: "alsa" no Linux)
    sfid = fs.sfload("../data/soundfont/GuitarA.sf2") 

    # Configure o sintetizador
    fs.program_select(0, sfid, 0, 0)  # Seleciona o programa/instrumento para canal 0 (pode variar)

    # Reproduza uma nota MIDI
    note = 60  # MIDI note C4
    velocity = 80  # Intensidade da nota (0 a 127)
    fs.noteon(0, note, velocity)

    # Aguarde um tempo (em segundos)
    mido.sleep(1)

    # Pare a nota
    fs.noteoff(0, note)

    # Finalize o sintetizador
    fs.delete()

if __name__ == "__main__":
    play_note()