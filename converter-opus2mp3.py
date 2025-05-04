from pydub import AudioSegment

# Substitua pelo caminho do seu arquivo renomeado
input_file = "audio.opus"  # ou .ogg, etc
output_file = "audio.mp3"

# Converte
audio = AudioSegment.from_file(input_file)
audio.export(output_file, format="mp3")

print("Arquivo convertido para MP3 com sucesso!")
