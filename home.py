import os
import tkinter
from tkinter import *
import sys
from PIL import Image, ImageTk
import wikipedia

def progress():
    print("In progress")

def pause():
    print("Paused.")    

def exit():
    print('Closing...')
    exit()

window = tkinter.Tk()

window.title('AI ASSISTANT')

window.geometry("793x750")
icon = os.path.join(sys.path[0], "logo.ico")
window.iconbitmap(icon)

start_button_img = PhotoImage(file= "START.png")
pause_button_img = PhotoImage(file= "PAUSE.png")
exit_button_img = PhotoImage(file= "EXIT.png")

canvas = Canvas(window, height = 2, width = 500)

canvas.pack(fill = BOTH, expand = True)

imageobj = ImageTk.PhotoImage(Image.open('Image.png'))

label_img = Label(canvas,
                   image = imageobj,
                     bg = "WHITE"
                     )

label_img.grid(column = 0, row = 0)

#Welcome_Label = Label()

Start_button = Button(window, 
                      image = start_button_img,
#                        background = "#EC1515", 
#                        foreground = "#FAFAF8",
#                        activebackground = "WHITE", 
#                        activeforeground="#EC1515", 
#                        highlightthickness= 2, 
#                        highlightbackground= "#EC1515", 
#                        highlightcolor= "WHITE", 
                        cursor= "hand1",
                        width = 315, 
                        height = 69, 
                        border = 0, 
                        command = progress
#                        font = ('Arial', 16, 'bold') 
)
Start_button.place(x = 0, y = 1)
Start_button.pack()

Pause_button = Button(window, 
                      image = pause_button_img,
#                        background = "#EC1515", 
#                        foreground = "#FAFAF8",
#                        activebackground = "WHITE", 
#                        activeforeground="#EC1515", 
#                        highlightthickness= 2, 
#                        highlightbackground= "#EC1515", 
#                        highlightcolor= "WHITE", 
                        cursor= "hand1",
                        width = 315, 
                        height = 69, 
                        border = 0, 
                        command = pause
#                        font = ('Arial', 16, 'bold') 
)
Pause_button.place(x = 0, y = 1)
Pause_button.pack()

exit_button = Button(window, 
                      image = exit_button_img,
#                        background = "#EC1515", 
#                        foreground = "#FAFAF8",
#                        activebackground = "WHITE", 
#                        activeforeground="#EC1515", 
#                        highlightthickness= 2, 
#                        highlightbackground= "#EC1515", 
#                        highlightcolor= "WHITE", 
                        cursor= "hand1",
                        width = 315, 
                        height = 69, 
                        border = 0, 
                        command = exit()
#                        font = ('Arial', 16, 'bold') 
)
exit_button.place(x = 0, y = 1)
exit_button.pack()

window.mainloop()