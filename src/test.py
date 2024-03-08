import sounddevice as sd
import numpy as np
import wave

def play_wav_file(file_path):
    # Read the WAV file
    wf = wave.open(file_path, 'rb')

    # Get WAV file parameters
    channels = wf.getnchannels()
    sample_width = wf.getsampwidth()
    frame_rate = wf.getframerate()
    frames = wf.getnframes()

    # Read audio data from the file
    audio_data = wf.readframes(frames)

    # Close the WAV file
    wf.close()

    # Convert bytes to NumPy array
    audio_array = np.frombuffer(audio_data, dtype=np.int16)

    # Play the audio
    sd.play(audio_array, samplerate=frame_rate)
    sd.wait()

if __name__ == "__main__":
    # Provide the path to your WAV file
    wav_file_path = "recorded_sound.wav"

    # Call the function to play the WAV file
    play_wav_file(wav_file_path)


