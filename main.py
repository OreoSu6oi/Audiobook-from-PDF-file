import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

book = askopenfilename()
reader = PdfReader(book)
pages = len(reader.pages)

player = pyttsx3.init()

for i in range(pages):
    page = reader.pages[i]
    text = page.extract_text()
    if text:
        player.say(text)
player.runAndWait()