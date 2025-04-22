import easygui as gui
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

def Rotator():
    # Display file selection dialog box
    pdf_path1 = gui.fileopenbox(title="select a PDF file", default="*.pdf")
    while pdf_path1 is None:
        break
    # select angle of rotation
    if pdf_path1:
        Angle2 = gui.enterbox(msg="Enter angle of rotation", title="Angle")
    
    while Angle2 == "":
        Angle2 = gui.enterbox(msg="Enter angle of rotation", title="Angle")
        
    while Angle2 is None:
         break
    
    if Angle2:        
        # Dialog box for displaying saving the rotated pdf
        file_path3 = gui.filesavebox(title="save_file", default="*.pdf")
        while file_path3 == pdf_path1:
            gui.msgbox(msg="use a different file name", title="file name")
            file_path3 = gui.filesavebox(title="save_file", default="*.pdf")
        if file_path3 is None:
                exit()

    # performing the page rotation
    pdf_reader = PdfReader(str(pdf_path1))
    Pdf_writer = PdfWriter()
    pages = pdf_reader.pages
    for page in pages:
        #if page["/Rotate"]:
        # print(page["/Rotate"])
        page.rotate(int(Angle2))
        Pdf_writer.add_page(page)
    with Path(file_path3).open(mode="wb") as output_file:
        Pdf_writer.write(output_file)


