import tkinter as tk
from tkinter import PhotoImage

background = (r"Prereq\Background.png")

# Main Tkinter Window
window = tk.Tk()
window.title("Forganizer")
window.geometry("400x200")
window.resizable(False, False)
background_image = PhotoImage(file=background) 
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)
# Labels
label_title = tk.Label(window, text="Forganiser")
label_title.pack(pady=10)

label_author = tk.Label(window, text="by Tom Porter")
label_author.pack(pady=4)

# Loop Window
window.mainloop()
