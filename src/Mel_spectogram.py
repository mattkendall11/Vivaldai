import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import wave

def generate_mel_spectrogram(file_path):
    # Read the WAV file
    wf = wave.open(file_path, 'rb')

    # Get WAV file parameters
    sample_rate = wf.getframerate()
    frames = wf.getnframes()

    # Read audio data from the file
    audio_data = wf.readframes(frames)

    # Close the WAV file
    wf.close()

    # Convert bytes to NumPy array
    audio_array = np.frombuffer(audio_data, dtype=np.int16)

    # Normalize audio data to the range [-1, 1]
    audio_array = audio_array.astype(np.float32) / np.iinfo(np.int16).max

    # Compute Mel-spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(y=audio_array, sr=sample_rate, n_fft=1024, hop_length=512, n_mels=128)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)

    # Display the Mel-spectrogram
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mel_spectrogram_db, x_axis='time', y_axis='mel', sr=sample_rate, hop_length=512, cmap='viridis')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-spectrogram')
    plt.show()

if __name__ == "__main__":
    # Provide the path to your WAV file
    wav_file_path = "recorded_sound.wav"

    # Call the function to generate and display the Mel-spectrogram
    generate_mel_spectrogram(wav_file_path)

