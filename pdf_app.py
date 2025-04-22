import tkinter as tk
from tkinter import font
from pdf_rotator import Rotator
from merger import Pdf_Merger
from pdf_Page_extractor import Page_extractor
from pdf_file_splitter import File_splitter
from encrypt import Encrypt
from converter import convert_docx_to_pdf

window  = tk.Tk()
window.title('PDF Editor')
window.columnconfigure(5, weight=1)
window.rowconfigure(4, weight=1)

Header_font = font.Font(family="Helvetica", size=30, weight="bold")
Btn_font = font.Font(family="Comic Sans MS", size=16, weight="bold")

frame = tk.Frame(master=window, bg="#488181", width=200, height=100)
frame.columnconfigure([1, 2, 3, 4, 5], minsize=100, weight=1)
frame.rowconfigure([1, 2, 3, 4], minsize=100, weight=1)
frame.grid(row=4, column=5, sticky='nsew')

label = tk.Label(master=frame, text="PDF EDITOR", bg="#488181", font=Header_font)
label.grid(row = 1, column=3, sticky="nnsew")
label.rowconfigure(4, weight=1)
label.columnconfigure(5, weight=1)

# rotate
rot_button = tk.Button(frame, text='Rotate', relief=tk.RAISED, height=3, border=5, font=Btn_font, command=Rotator)
rot_button.grid(row=2, column=1)

# merge
merge_button = tk.Button(frame, text='Merge', relief=tk.RIDGE, width=5, height=3, border=5, font=Btn_font, command=Pdf_Merger)
merge_button.grid(row=2, column=2, padx=5, pady=10)

# extract page
extract_button = tk.Button(frame, text='Extract pages', relief=tk.GROOVE, height=3, border=5, font=Btn_font, command=Page_extractor)
extract_button.grid(row=2, column=3)

# split page
split = tk.Button(frame, text='Split', relief=tk.GROOVE, height=3, border=5, font=Btn_font, command=File_splitter)
split.grid(row=2, column=4)

# Encrypt
secure_button = tk.Button(frame, text='Encrypt', relief=tk.SUNKEN, height=3, border=5, font=Btn_font, command=Encrypt)
secure_button.grid(row=2, column=5)

# Convert .doc(x) to PDF
converter_button = tk.Button(frame, text='Word to PDF', relief=tk.SUNKEN, height=3, border=5, font=Btn_font, command=convert_docx_to_pdf)
converter_button.grid(row=3, column=1)

window.mainloop()