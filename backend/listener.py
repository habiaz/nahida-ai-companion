import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

duration = 5
sample_rate = 16000

print("Recording... 🎙️")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate = sample_rate,
    channels = 1,
    dtype = "float32"
) 

sd.wait()

model = WhisperModel(
    "small",
    device="cuda",
    compute_type="float16"
) ## ghi âm với cuda từ nvidia nè 

print("Whisper model loaded!")

print("Peak amplitude:", np.max(np.abs(audio)))

print("Recording finished!")

segments, info = model.transcribe(
    audio.flatten(),
    beam_size=5
)

for segment in segments:
    print(segment.text)
