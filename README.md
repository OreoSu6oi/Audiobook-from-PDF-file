# Audiobook from PDF

A simple Python program that converts a PDF file into an audiobook using text-to-speech.

---

## Features

- Select any PDF file using a file dialog.
- Extracts text from each page of the PDF.
- Converts the extracted text into speech using `pyttsx3`.
- Plays the audiobook directly through your system audio.

---

## Requirements

- Python 3.7 or higher
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- Tkinter (for the file dialog GUI)

Install the dependencies using pip:

```bash
pip install pyttsx3 PyPDF2
