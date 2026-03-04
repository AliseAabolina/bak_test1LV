from transformers import VitsModel, AutoTokenizer
import torch
import soundfile as sf

# Ielādē modeli un teksta apstrādātāju (tokenizer)
model_name = "facebook/mms-tts-lav"
model = VitsModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Ievadi savu latviešu tekstu
text = "Sveika, pasaule! Šis ir tests ar latviešu valodas modeli."

# Apstrādā tekstu un ģenerē runu
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    output = model(**inputs).waveform

# Izvadi kā WAV failu (sampling rate 16000 Hz)
import os
output_path = os.path.expanduser("~/Desktop/latviesu_runa.wav")
sf.write(output_path, output.squeeze().numpy(), samplerate=16000)
print(f"Audio fails saglabāts kā: {output_path}")