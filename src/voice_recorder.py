import pyaudio
import wave

audio = pyaudio.PyAudio()

AUDIO_FORMAT = pyaudio.paInt16
NO_OF_AUDIO_CHANNEL=1
STREAM_RATE = 44100
FRAMES_PER_BUFFER = 1024

OUTPUT_FILENAME = "output.wav"
frames = []

def get_stream():
    stream = audio.open(
        format=AUDIO_FORMAT,
        channels=NO_OF_AUDIO_CHANNEL,
        rate=STREAM_RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER,
    )
    return stream

def generate_audio_file():
    output_wf = wave.open(OUTPUT_FILENAME, "wb")
    output_wf.setnchannels(NO_OF_AUDIO_CHANNEL)
    output_wf.setsampwidth(audio.get_sample_size(AUDIO_FORMAT))
    output_wf.setframerate(STREAM_RATE)
    output_wf.writeframes(b"".join(frames))
    output_wf.close()
    return output_wf


def record_audio():
    try:
        stream = get_stream()
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        pass

    try:
        stream.stop_stream()
        stream.close()
        audio.terminate()
    except:
        print('Exception in record_audio')

    return generate_audio_file()


def main():
    record_audio()


if __name__ == "__main__":
    main()
    






