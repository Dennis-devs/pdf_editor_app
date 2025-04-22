from spire.doc import *
from spire.doc.common import *
import easygui as gui
from docx2pdf import convert

def convert_docx_to_pdf():
    # Converts selected DOCX file(s) to PDF.
    
    docx_files = gui.fileopenbox(title="Select file(s)", filetypes=["*.docx", "*.doc"], multiple=True) 
    #iterate returned list of files(s)
    for word_files in docx_files:   
        print(word_files)
        pdf_files = gui.filesavebox(title="save file(s)", default="*.pdf")

        try:
            convert(word_files, pdf_files)
            print(f"Converted: {word_files} to {pdf_files}")
        except Exception as e:
            print(f"Error converting {word_files}: {e}")


