from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import easygui as gui

def Encrypt():
    file_path = gui.fileopenbox(title="file select", msg="select file to encrypt",  default='*.pdf')
    
    pdf_reader = PdfReader(file_path)
    
    pdf_writer = PdfWriter()
    pdf_writer.append_pages_from_reader(pdf_reader)
    
    password = gui.enterbox(title="Password", msg="Enter your password")
    pdf_writer.encrypt(user_pwd=password)
    
    encrypted_file = gui.filesavebox(title="file save", msg="Save file", default='*.pdf')
    
    with Path(encrypted_file).open(mode="wb") as output_file:
        pdf_writer.write(output_file)