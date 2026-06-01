# Install required libraries
!pip install transformers torch librosa gtts -q

from google.colab import files
from transformers import pipeline
from gtts import gTTS
from IPython.display import Audio
import librosa # Import librosa

# ============================
# Upload Audio File
# ============================
print("Upload your MP3 file")
uploaded = files.upload()

audio_file_path = list(uploaded.keys())[0]

print("Audio Loaded:", audio_file_path)

# ============================
# Audio → Text (Whisper)
# ============================
print("\nConverting Audio to Text...")

asr = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
    chunk_length_s=None, # Explicitly disable chunking
    return_timestamps=True # Enable timestamp prediction for long audio
)

# Load audio using librosa
audio, sr = librosa.load(audio_file_path, sr=16000) # Whisper models usually expect 16kHz

# Convert audio to text, passing raw audio and sampling rate
text = asr({"array": audio, "sampling_rate": sr})["text"]

print("\nRecognized Text:")
print(text)

# ============================
# Sentiment Analysis
# ============================
print("\nAnalyzing Sentiment...")

sentiment_model = pipeline(
    "sentiment-analysis"
)

result = sentiment_model(text)[0]

label = result["label"]
confidence = result["score"]

print("\nSentiment:", label)
print("Confidence:", confidence)

# Prepare output sentence
if label == "POSITIVE":
    output_text = f"The sentiment is positive with confidence {confidence:.2f}"
else:
    output_text = f"The sentiment is negative with confidence {confidence:.2f}"

print("\nFinal Message:")
print(output_text)

# ============================
# Text → Audio (gTTS)
# ============================
tts = gTTS(output_text)

output_audio = "final_result.mp3"

tts.save(output_audio)

print("\nPlaying Final Audio:")

Audio(output_audio)
