# Audio Transcription Script

This script converts audio files (even WhatsApp `.dat.unknown` files) to MP3 and transcribes them using OpenAI's Whisper.

## ✅ Requirements

- Python 3.8+
- FFmpeg installed and added to your system PATH
- Whisper and pydub installed

## 📦 Installation

1. **Install FFmpeg**

   Download the full version of FFmpeg from: https://www.gyan.dev/ffmpeg/builds/

   - Extract it to `C:\ffmpeg` (or any folder)
   - Add the `C:\ffmpeg\ffmpeg-<version>\bin` folder to your system PATH

   To verify it’s working, open a terminal and run:

   ```bash
   ffmpeg -version
   ffprobe -version
   ```

2. **Install Python packages**

   ```bash
   pip install pydub git+https://github.com/openai/whisper.git
   ```

## ▶️ Usage

1. Place your audio file in the same folder as the script.
2. Update the `original_file` and `input_format` variables in `transcribe_audio.py` if needed.
3. Run the script:

   ```bash
   python transcribe_audio.py
   ```

The transcription will be saved in a `transcription.txt` file.

---

**Note:** Whisper runs slower on CPU. You can try other models by changing `base` to `small`, `medium`, or `large` for better accuracy (but slower speed).