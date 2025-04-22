import easygui as gui
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

def Page_extractor():
    # select a file to open
    file_opener = gui.fileopenbox(title="select a file")
    if file_opener is None:
        exit()

    # Entering start page
    start_page = gui.enterbox(msg="Enter starting page", title="pager")
    start_page = int(start_page)
    if start_page is None:
        exit()
    while start_page < 0:
        gui.msgbox(msg="Invalid entry. Enter a positive number")
        start_page = gui.enterbox(msg="Enter starting page", title="pager")
        if start_page is None:
            exit()
        start_page = int(start_page)


    # Entering end page
    end_page = gui.enterbox(msg="Enter End page", title="pager")
    end_page = int(end_page)
    if end_page is None:
        exit()
    while end_page < 0:
        gui.msgbox(msg="Invalid entry. Enter a positive number")
        end_page = gui.enterbox(msg="Enter End page", title="pager")
        if end_page is None:
            exit()
        end_page = int(end_page)


    # save file
    file_saver = gui.filesavebox(title="file saver", default="*.pdf")
    if file_saver is None:
            exit()
    while file_saver == file_opener:
         gui.msgbox(msg="Input file cant be overwritten. select another location") 
         file_saver = gui.filesavebox(title="file saver", default="*.pdf")
         if file_saver is None:
            exit()  

    pdf_reader = PdfReader(file_opener)   
    pdf_writer = PdfWriter()
    pages = pdf_reader.pages  

    for n in range(start_page, end_page):
        pages = pdf_reader.pages[n]
        pdf_writer.add_page(pages)    
    with open(file_saver, "wb") as output_file:
        pdf_writer.write(output_file)