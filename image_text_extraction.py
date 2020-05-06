from tkinter import *
import pytesseract as pyt
import numpy as np
import cv2
import imutils
from PIL import Image
from tkinter import scrolledtext
from gtts import gTTS
import os

pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def exit_button():
    root.destroy()


def clear_text():
    textbar.delete('1.0', END)


def image_extract():
    path = entry.get()
    print(path)
    img_show = cv2.imread(r'' + path + '')
    img_show = imutils.resize(img_show, width=300)
    cv2.imshow('Input Image', img_show)
    img = Image.open(r'' + path + '')
    text = pyt.image_to_string(img)
    textbar.insert(INSERT, text)


def convert_to_audio():
    result = textbar.get(1.0, END)
    mytext = result
    language = 'en'
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")


def licenseplate():
    try:
        path = entry.get()
        img = cv2.imread(r'' + path + '')  # Example: C:\Users\User\Desktop\image.png
        print(path)
        img = imutils.resize(img, width=300)
        cv2.imshow('Input Image', img)
        grey_version = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grey_version = cv2.bilateralFilter(grey_version, 11, 17, 17)
        edges = cv2.Canny(grey_version, 170, 200)
        cv2.imshow('', edges)
        contours, new = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
        Numberplate = None

        for j in contours:
            p = cv2.arcLength(j, True)
            apprx = cv2.approxPolyDP(j, 0.02 * p, True)
            if len(apprx) == 4:
                Numberplate = apprx
                break

        masked = np.zeros(grey_version.shape, np.uint8)
        new_img = cv2.drawContours(masked, [Numberplate], 0, 255, -1)
        new_img = cv2.bitwise_and(img, img, mask=masked)
        cv2.imshow('', new_img)
        text = pyt.image_to_string(new_img)
        textbar.insert(INSERT, text + "\n")

    except:
        text = "not able to extract, sorry!"
        textbar.insert(INSERT, text)


def on_entry_click(event):
    if entry.get() == 'Enter the path of your image':
        entry.delete(0, "end")
        entry.insert(0, '')


root = Tk()
menubar = Menu(root)
root.config(menu=menubar)
sub = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=sub)
sub.add_command(label="Exit", command=exit_button)
sub.add_command(label="Clear Text", command=clear_text)
sub = Menu(menubar, tearoff=0)

entry = Entry(root, width=30, bd=3)
entry.insert(0, "Enter the path of your image")
entry.bind('<FocusIn>', on_entry_click)
entry.place(x=80, y=390)
button = Button(root, text="Is It a License Plate?", command=licenseplate).place(x=430, y=130)
button1 = Button(root, text="Is It an Image with Texts?", command=image_extract).place(x=430, y=180)
button2 = Button(root, text="Convert Text to Audio", command=convert_to_audio).place(x=430, y=230)
Label(root,
      text="TEXT Extraction \n From IMAGE",
      bg="black",
      fg="white",
      font="Verdana 20 bold").place(x=180, y=25)
textbar = scrolledtext.ScrolledText(
    width=40,
    height=15,
    bd=4,
    font="Times 10 bold"
)
statusbar = Label(root, text="Wronmber Tech Labs", relief=SUNKEN,
                  anchor=W)
statusbar.place(x=480, y=480)
textbar.place(x=60, y=120)
root.resizable(0, 0)
root.title("Text Extractor")
root.geometry("600x500+120+200")
root.config(bg="black")
root.mainloop()
