import tkinter as tk
from tkinter import PhotoImage
import subprocess

background = (r"C:\Dev\Forganizer-\Prereq")

# Tools
def DocOrg():
    file_path = 'Tools/Documents.py'
    subprocess.run(["python", file_path])
def DowOrg():
    file_path = 'Tools/Downloads.py'
    subprocess.run(["python", file_path])
def PicOrg():
    file_path = 'Tools/Pictures.py'
    subprocess.run(["python", file_path])

# Main Tkinter Window
window = tk.Tk()
window.title("Forganizer by Tom Porter")
window.geometry("410x100")
window.resizable(False, False)
background_image = PhotoImage(file= background)
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Labels
label_title = tk.Label(window, text="Forganiser")
label_title.grid(row=0, column=0, columnspan=2, pady=10)


# Buttons
button1 = tk.Button(window, text="Document Organiser", command=DocOrg)
button1.grid(row=2, column=1, pady=10, padx=10, sticky="w")
button2 = tk.Button(window, text="Downloads Organiser", command=DowOrg)
button2.grid(row=2, column=2, pady=10, padx=10)
button3 = tk.Button(window, text="Pictures Organiser", command=PicOrg)
button3.grid(row=2, column=3, pady=10, padx=10)

# Loop Window
window.mainloop()
