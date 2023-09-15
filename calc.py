from tkinter import *
ob=Tk()
# ob.geometry('300x300')

exp=""
def handleclick(button):
    global exp
    if len(exp)==0:
        if button.isdigit():
            if button!="0":
                exp=exp+button
                data.set(exp)
           

    else:
        exp=exp+button
        data.set(exp)

def handleequal():
    global exp
    if exp[-1].isdigit():
        res=eval(exp)
        data.set(res)
        exp=""

def handlebackspace():
    global exp
    exp=exp[:-1]
    data.set(exp)
    print(exp)
    
data=StringVar()

input_box=Entry(ob,font=28,textvariable=data)
input_box.grid(row=0,column=0,columnspan=4,pady=10)

button=Button(ob,text="1",font=28,padx=10,pady=10,command=lambda: handleclick("1"))
button.grid(row=3,column=0,padx=10,pady=10)
button=Button(ob,text="2",font=28,padx=10,pady=10,command=lambda: handleclick("2"))
button.grid(row=3,column=1,padx=10,pady=10)
button=Button(ob,text="3",font=28,padx=10,pady=10,command=lambda: handleclick("3"))
button.grid(row=3,column=2,padx=10,pady=10)

button=Button(ob,text="4",font=28,padx=10,pady=10,command=lambda: handleclick("4"))
button.grid(row=2,column=0,padx=10,pady=10)
button=Button(ob,text="5",font=28,padx=10,pady=10,command=lambda: handleclick("5"))
button.grid(row=2,column=1,padx=10,pady=10)
button=Button(ob,text="6",font=28,padx=10,pady=10,command=lambda: handleclick("6"))
button.grid(row=2,column=2,padx=10,pady=10)

button=Button(ob,text="7",font=28,padx=10,pady=10,command=lambda: handleclick("7"))
button.grid(row=1,column=0,padx=10,pady=10)
button=Button(ob,text="8",font=28,padx=10,pady=10,command=lambda: handleclick("8"))
button.grid(row=1,column=1,padx=10,pady=10)
button=Button(ob,text="9",font=28,padx=10,pady=10,command=lambda: handleclick("9"))
button.grid(row=1,column=2,padx=10,pady=10)
button=Button(ob,text="0",font=28,padx=10,pady=10,command=lambda: handleclick("0"))
button.grid(row=4,column=1,padx=10,pady=10)

button=Button(ob,text="*",padx=10,pady=10,font=28,command=lambda: handleclick("*"))
button.grid(row=1,column=3,padx=10,pady=10)

button=Button(ob,text="+",padx=10,pady=10,font=28,command=lambda: handleclick("+"))
button.grid(row=2,column=3,padx=10,pady=10)
button=Button(ob,text="-",padx=10,pady=10,font=28,command=lambda: handleclick("-"))
button.grid(row=3,column=3,padx=10,pady=10)
button=Button(ob,text="/",padx=10,pady=10,font=28,command=lambda: handleclick("/"))
button.grid(row=4,column=3,padx=10,pady=10)

button=Button(ob,text="=",padx=10,pady=10,font=28,command=handleequal)
button.grid(row=4,column=2,padx=10,pady=10)

button=Button(ob,text="cl",padx=10,pady=10,font=28,command=handlebackspace)
button.grid(row=4,column=0,padx=10,pady=10)
ob.mainloop()

