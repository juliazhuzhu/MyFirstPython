import tkinter

window = tkinter.Tk()

window['background'] = 'blue'
w = 300
h = 200
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2)-(w/2)
y = (hs/2)-(h/2)

window.title('hello world')
window.geometry('%dx%d+%d+%d'%(w,h,x,y))
label = tkinter.Label(window,text="古北水镇")
label.pack()
tkinter.mainloop()