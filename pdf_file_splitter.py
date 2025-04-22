from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import easygui as gui

def File_splitter():
    class PdfFileSplitter:
        def __init__(self, pdf_path):
            self.pdf_reader = PdfReader(pdf_path)
            self.writer1 = None
            self.writer2 = None

        def split(self, breakpoint):
            self.writer1 = PdfWriter()
            self.writer2 = PdfWriter()

            for page in self.pdf_reader.pages[:breakpoint]:
                self.writer1.add_page(page)

            for page in self.pdf_reader.pages[breakpoint:]:
                self.writer2.add_page(page)   

        def write(self, filename):

            with Path(filename + '_1.pdf').open(mode='wb') as output_file:
                self.writer1.write(output_file)

            with Path(filename + '_2.pdf').open(mode='wb') as output_file:
                self.writer2.write(output_file)


    file_path =  gui.fileopenbox(title="Select a file", default='*.pdf')

    pdf_splitter = PdfFileSplitter(file_path)

    break_point = gui.enterbox(msg="Enter page break point", title="Break Point")

    pdf_splitter.split(int(break_point))

    split_files = gui.filesavebox(title="Save split files")

    pdf_splitter.write(split_files)       