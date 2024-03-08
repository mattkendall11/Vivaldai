from src.record import record
from src.Mel_spectogram import generate_mel_spectrogram

'''
main script to excecute the app functionality
'''
record()
generate_mel_spectrogram('src/recorded_sound.wav')

