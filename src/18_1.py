import tkinter as tk

window = tk.Tk()
window.title('登录窗口')
window.geometry('600x400')


def login():
    print(entryVar1.get())
    print(entryVar2.get())
    
lable_texts = ("User Name:","Password:")
i = 0
for _text in lable_texts:
    i = i+1
    _label = tk.Label(window,text=_text)
    _label.place(x=15,y=30+i*25,width=72,height=25)
    if i == 1:
        entryVar1=tk.StringVar()
        entry1 = tk.Entry(window,textvariable=entryVar1)
    else:
        entryVar2=tk.StringVar()
        entry1 = tk.Entry(window,textvariable=entryVar2,show="*")
    entry1.place(x=100,y=30+i*25,width=150,height=25)
    #_label.pack(fill=tk.X,ipadx=10,ipady=5,padx=10,pady=10)
    

button1 = tk.Button(window,text="登录",command=login)
button1.place(x=130,y=120)
button2 = tk.Button(window,text="取消",command=window.quit)
button2.place(x=190,y=120)

window.mainloop()