from turtle import Turtle, Screen
import ctypes 
from PIL import Image
from tkinter import messagebox
import cv2
import numpy as np

def preprocess():
    img = cv2.imread("letter.jpg")
    ## (1) Convert to gray, and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    ## (2) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

## (3) Find the max-area contour
    cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]
        ## Chnage color depth
       
## (4) Crop and save it
    x,y,w,h = cv2.boundingRect(cnt)
    dst = img[(y-10):y+(h+10), (x-10):x+(w+10)] 
    i=cv2.resize(dst, (28, 28)) 
    cv2.imwrite("letter.jpg", i)
    img1 = Image.open("letter.jpg")
    img2 = img1.convert(colors=8)
    img2.save('letter.png', quality=90, lossless = True,mode='L')
        #imgNew.thumbnail((2000,2000), Image.ANTIALIAS)
        #newsize = (45, 45)
        #width, height = imgNew.size
        #print(width,height)
        #cropped = imgNew.crop((169, 193, width-170, height-194))
        #cropped.save('letter.png', quality=90, lossless = True)
        #width, height = cropped.size
        #print(width,height)
        #imgNew = Image.open("letter1.png")
        #img=imgNew.resize([32,32])
        #img.save('letter.png', quality=90, lossless = True)
        
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