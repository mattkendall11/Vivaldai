import keyboard
import sounddevice as sd
import numpy as np
import wave

def record(output_filename="recorded_sound.wav", duration=5, sample_rate=44100):
    # Initialize recording variables
    recording = False
    audio_data = []

    def on_space(event):
        nonlocal recording, audio_data
        if event.event_type == keyboard.KEY_DOWN:
            if not recording:
                print("Recording started. Press space again to stop.")
                recording = True
                audio_data = []
                record_audio()

    def record_audio():
        nonlocal audio_data
        with sd.InputStream(callback=lambda indata, frames, time, status: audio_data.extend(indata.tobytes())) as stream:
            sd.sleep(int(duration * 1000))
        save_audio_file(audio_data)

    def save_audio_file(data):
        with wave.open(output_filename, 'w') as wf:
            wf.setnchannels(1)  # Mono audio
            wf.setsampwidth(2)  # 16-bit audio
            wf.setframerate(sample_rate)
            wf.writeframes(np.array(data).tobytes())

    # Register the space bar event handler
    keyboard.on_press_key("space", on_space)

    # Start the recording loop
    print("Press space to start recording.")
    keyboard.wait("space")
    keyboard.unhook_all()
    print("Recording completed. Audio saved as '{}'.".format(output_filename))




