from pathlib import Path
from PyPDF2 import PdfMerger
import easygui as gui

def Pdf_Merger():
    # select files to merge
    files_to_merge = gui.fileopenbox(title="File Explorer", msg="Select File(s)", default='*.pdf', multiple=True)

    pdf_merger = PdfMerger()
    for path in files_to_merge:
        pdf_merger.append(str(path))

    # save file
    save_file_path = gui.filesavebox(title="Save file", default='*.pdf')

    while save_file_path == any(files_to_merge):
        gui.msgbox(msg='Enter a different file name', title='file_name')

        save_file_path = gui.filesavebox(title="Save file", default='*.pdf')

    if save_file_path is None:
        exit()

    with Path(save_file_path).open(mode="wb") as output_file:
        pdf_merger.write(output_file)
