from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    BMI= float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    BMI=0
    print(BMI)
    if BMI>30.0 :
        labelResult.configure(text="อ้วนมาก")
    elif 25.0 <BMI< 29.9 :
        labelResult.configure(text="อ้วน")
    elif 23.0 <BMI< 24.9 :
        labelResult.configure(text="น้ำหนักเกิน")
    elif 18.6 <BMI< 22.9 :
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labelResult.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (cm.)",width=13,fg="white",bg="blue")
labelHeight.grid(row=0, column=0)
textBoxHeight= Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (kg.)",width=13,fg="white",bg="blue")
labelWeight.grid(row=1, column=0)
textBoxWeight= Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow,text="คำนวณ",fg="black",bg="white")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult= Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()