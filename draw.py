from turtle import Turtle, Screen
import ctypes 
from PIL import Image
from tkinter import messagebox
import cv2
import numpy as np
def dialogue(x,y):
    r=ctypes.windll.user32.MessageBoxW(0, "Do you wish to continue?", "Dialogue Box", 6)
    #print(r)
    if r ==2:
        screen.bye()
    elif r == 10:
        #yertle.clear()
        yertle.reset()
        #screen.resetscreen()
        yertle.speed('fast')
        yertle.pensize(5)
        yertle.turtlesize(stretch_wid=2, stretch_len=2, outline=5)
        #yertle.onclick(dragging)
    elif r == 11:
        yertle.hideturtle()
        ts = yertle.getscreen()
        ts.getcanvas().postscript(file="letter.eps")
        imgNew = Image.open("letter.eps")
        #imgNew.convert("RGBA")
        imgNew.save('letter1.png', quality=90, lossless = True)
        messagebox.showinfo("Message Box", "Drawing saved as image file successfully.")
    else:
        print("Some error occured")
def dragging(x, y):
    yertle.ondrag(None)
    #yertle.setheading(yertle.towards(x, y))
    yertle.goto(x, y)
    yertle.ondrag(dragging)

screen = Screen()
#screen.bgcolor("orange")
yertle = Turtle('classic')
screen.register_shape("pen1.gif")
yertle.shape("pen1.gif")
yertle.speed('fast')
screen.title("Draw characters here")
yertle.pensize(5)
#yertle.pencolor("white")
yertle.turtlesize(stretch_wid=2, stretch_len=2, outline=5)
yertle.onclick(dragging)
yertle.onrelease(dialogue, btn=1, add=None)
screen.mainloop()

#C:\Program Files\Common Files\Oracle\Java\javapath;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files\Skype\Phone\;C:\Program Files\GtkSharp\2.12\bin;C:\Program Files\Git\cmd
