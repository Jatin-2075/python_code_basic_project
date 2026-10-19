from tkinter import *
from PIL import Image, ImageTk

mine_root = Tk()

# Load the image properly with Pillow
image = Image.open("8672905.jpg")  # Ensure the file exists
photo = ImageTk.PhotoImage(image)

first_label = Label(mine_root, image=photo)
first_label.pack()

# Keep a reference to the image to prevent garbage collection
first_label.image = photo

mine_root.mainloop()
