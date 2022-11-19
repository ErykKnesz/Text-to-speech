import os
import sys

import requests
from PyPDF2 import PdfReader

API_BASE_URL = "http://api.voicerss.org/"
API_KEY = os.getenv("API_KEY")
MAX_CHARACTERS = 1000

pdf_file_path = sys.argv[1]
pdf_language = sys.argv[2] if len(sys.argv) > 2 else "pl-pl"

reader = PdfReader(pdf_file_path)
text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

with open("pdftext", "w") as file:
    file.write(text)


def crop_text(text):
    if len(text) > MAX_CHARACTERS:
        return (text[i:i + MAX_CHARACTERS]
                for i in range(0, len(text), MAX_CHARACTERS))


def get_speech_from_text(text, language="pl-pl", audio_codec='MP3'):
    for chunk in crop_text(text):
        params = {
            "key": API_KEY,
            "src": chunk,
            "c": audio_codec,
            "hl": language
        }
        req = requests.get(API_BASE_URL, params=params, stream=True)
        with open("new_mp3.mp3", 'ab') as file:
            for chunk in req.iter_content(chunk_size=128):
                file.write(chunk)


if __name__ == "__main__":
    get_speech_from_text(text, pdf_language)
