import PyPDF2
from gtts import gTTS
import os


def pdf_to_speech(pdf_path, output_path):

    with open(pdf_path, 'rb') as file:

        pdf_reader = PyPDF2.PdfReader(file)

        text = ""
        for page in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page]
            text += page_obj.extract_text()

        tts = gTTS(text)

        tts.save(output_path)


pdf_path = 'cheat_sheet.pdf'
output_path = 'cheat_sheet.mp3'

pdf_to_speech(pdf_path, output_path)
