import os
import warnings
from pydub import AudioSegment
import whisper

# Suppress warnings like "FP16 is not supported on CPU"
warnings.filterwarnings("ignore")

# === CONFIGURATION ===
original_file = "audio.opus"  
#input_format = "opus"  
converted_file = "audio.mp3"
language = "Portuguese"
output_txt = "transcription.txt"

# === CONVERT TO MP3 ===
print("🔄 Converting to MP3...")
audio = AudioSegment.from_file(original_file)
audio.export(converted_file, format="mp3")
print("✅ Conversion completed.")

# === TRANSCRIBE WITH WHISPER ===
print("🧠 Transcribing with Whisper...")
model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
result = model.transcribe(converted_file, language=language)
text = result["text"]

# === SAVE TRANSCRIPTION TO FILE ===
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(text)

print(f"📄 Transcription saved to: {output_txt}")
