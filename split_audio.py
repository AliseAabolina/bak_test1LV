import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Norādi ceļu uz ffmpeg (pielāgo savam datoram!)
ffmpeg_path = r"C:\Users\Unreal User\Downloads\ffmpeg\ffmpeg-2026-03-09-git-9b7439c31b-essentials_build\ffmpeg-2026-03-09-git-9b7439c31b-essentials_build\bin\ffmpeg.exe"
AudioSegment.converter = ffmpeg_path

# Ievades faila nosaukums – pārliecinies, ka tas precīzi atbilst!
input_file = "Jaunā Derība _ jaunā tulkojumā _ audio _ 1. daļa. [eu5yljNfaLE].wav"
output_dir = "wavs"

# Pārbaudi, vai fails eksistē
if not os.path.exists(input_file):
    print(f"Kļūda: fails '{input_file}' nav atrasts!")
    print("Pārbaudi nosaukumu un mēģini vēlreiz.")
    exit()

print("Ielādē audio...")
audio = AudioSegment.from_wav(input_file)

# Parametri sadalīšanai pēc klusuma
min_silence_len = 500   # minimālais klusuma garums (ms)
silence_thresh = -40    # klusuma slieksnis (dB)
keep_silence = 200      # cik daudz klusuma paturēt (ms)

print("Sāk sadalīšanu...")
chunks = split_on_silence(
    audio,
    min_silence_len=min_silence_len,
    silence_thresh=silence_thresh,
    keep_silence=keep_silence
)

print(f"Iegūti {len(chunks)} fragmenti.")

# Saglabā fragmentus
for i, chunk in enumerate(chunks):
    if len(chunk) < 2000:  # izlaiž īsākus par 2 sek.
        continue
    output_filename = os.path.join(output_dir, f"fragments_{i:04d}.wav")
    chunk.export(output_filename, format="wav")
    print(f"Saglabāts: {output_filename}")

print("Pabeigts!")