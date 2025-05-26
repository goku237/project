from tkinter import *
root = Tk()
root.title('Simple Calculator')
e = Entry(width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

def ButtonClick(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def ButtonClear():
    e.delete(0,END)

def ButtonAdd():
    global math
    global fnum
    math = 1
    first_number = e.get()
    fnum= int(first_number)
    e.delete(0,END)

def ButtonSub():
    global math
    global fnum
    math = 2
    first_number = e.get()
    fnum= int(first_number)
    e.delete(0,END)

def ButtonMul():
    global fnum
    global math 
    math =3
    first_number = e.get()
    fnum= int(first_number)
    e.delete(0,END)

def ButtonDiv():
    global fnum
    global math 
    math = 4
    first_number = e.get()
    fnum= int(first_number)
    e.delete(0,END)

def ButtonEqual():
    second_number = e.get()
    e.delete(0,END)

    if math == 1:
        e.insert(0,int(second_number)+fnum)

    elif math == 2:
        e.insert(0,fnum - int(second_number))

    elif math == 3:
        e.insert(0,int(second_number) * fnum)

    else:
        e.insert(0,fnum/int(second_number))

        print("hello")

button1 = Button(root,text=1,padx=40,pady=20,command= lambda: ButtonClick(1)).grid(row=1,column=0)
button2 = Button(root,text=2,padx=40,pady=20,command= lambda: ButtonClick(2)).grid(row=1,column=1)
button3 = Button(root,text=3,padx=40,pady=20,command= lambda: ButtonClick(3)).grid(row=1,column=2)

button4 = Button(root,text=4,padx=40,pady=20,command= lambda: ButtonClick(4)).grid(row=2,column=0)
button5 = Button(root,text=5,padx=40,pady=20,command= lambda: ButtonClick(5)).grid(row=2,column=1)
button6 = Button(root,text=6,padx=40,pady=20,command= lambda: ButtonClick(6)).grid(row=2,column=2)

button7 = Button(root,text=7,padx=40,pady=20,command= lambda: ButtonClick(7)).grid(row=3,column=0)
button8 = Button(root,text=8,padx=40,pady=20,command= lambda: ButtonClick(8)).grid(row=3,column=1)
button9 = Button(root,text=9,padx=40,pady=20,command= lambda: ButtonClick(9)).grid(row=3,column=2)

button0 = Button(root,text=0,padx=40,pady=20,command= lambda: ButtonClick(0)).grid(row=4,column=0)
buttonClear = Button(root, text='Clear',padx=77,pady=20,command= ButtonClear).grid(row=4,column=1,columnspan=2)
buttonEqual = Button(root,text="=",padx=87,pady=20,command=ButtonEqual).grid(row=5,column=1,columnspan=2)
buttonAdd = Button(root,text="+",padx=39,pady=20,command= ButtonAdd).grid(row=5,column=0)

buttonSub = Button(root,text="-",padx=40,pady=20,command= ButtonSub).grid(row=6,column=0)
buttonMul = Button(root,text="*",padx=41,pady=20,command= ButtonMul).grid(row=6,column=1)
buttonDiv = Button(root,text="/",padx=40,pady=20,command= ButtonDiv).grid(row=6,column=2)

root.mainloop()
