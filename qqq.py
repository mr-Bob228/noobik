from PIL import Image
from customtkinter import *

win = CTk()
win.title(Image)
win.geometry("400x400")

img = Image.open("michael-sum-LEpfefQf4rU-unsplash.jpg")
img_ctk = CTkImage(light_image=img, size=(300, 300))

label = CTkLabel(win, text="", image=img_ctk)
label.pack(pady=10)
win.mainloop()