import PyPDF2
from gtts import gTTS
import os


def pdf_to_speech(pdf_path, output_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Initialize PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Extract text from each page
        text = ""
        for page in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page]
            text += page_obj.extract_text()

        # Create a gTTS object with the extracted text
        tts = gTTS(text)

        # Save the speech as an MP3 file
        tts.save(output_path)


# Provide the paths for the input PDF file and output speech file
pdf_path = 'cheat_sheet.pdf'
output_path = 'cheat_sheet.mp3'

# Convert the PDF to speech
pdf_to_speech(pdf_path, output_path)
