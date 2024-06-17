import tkinter
import random
import tkinter.font
window = tkinter.Tk()
window.title("ff")
window.geometry('1000x700+100+100')

def btn2_event():
    font = tkinter.font.Font(family='맑은 고딕',size=20)
    label = tkinter.Label(window,text=str(a),font=font)
    label["compound"] = "bottom"
    label.pack()


alist=[]
a = 0
#기능 구현(버튼)

def btn2_event():
    global a

    

    if len(alist) < int(entry3.get()):
        a = int(random.randrange(1,int(entry3.get())+1))
        while a in alist:
            a = int(random.randrange(1,int(entry3.get())+1))
        alist.append(a)
        print(a)
        label.config(text = a)
    else:
        print('다 나왔음')
        label.config(text = "끝")

image=tkinter.PhotoImage(file="배경.png")
background = tkinter.Label(image=image)
background.place(x=0, y=0)

photo1 = tkinter.PhotoImage(file="대포알.png")
label=tkinter.Label(window,width=250, height=250, fg="red", relief="solid",image=photo1)
label.pack()

label3 = tkinter.Label(window,text='숫자입력')
entry3 = tkinter.Entry(window)
label3.pack()
entry3.pack()


photo2 = tkinter.PhotoImage(file="대포1.png")
btn = tkinter.Button(window, overrelief="flat", width=300,height=300, repeatdelay=1000, repeatinterval=100,image=photo2, command=btn2_event)
btn.pack(side='bottom')
btn.pack()

number_font = tkinter.font.Font(family='맑은 고딕',size=100)
label = tkinter.Label(text='0', font=number_font)
label.place(x=445, y=20)

window.mainloop()
