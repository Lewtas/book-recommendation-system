import tkinter as tk
import NBC


def recBook():
    global entry1, result_label
    str1 = NBC.toBook(entry1.get())
    s = 'Book for you:\n'
    for i in str1:
        s += i
        s += '\n'
    result_label.config(text=s, font='20')
    result_label.place(x=120, y=50)
    return s


root = tk.Tk()
canvas1 = tk.Canvas(root, width=1200, height=720, bg='lightsteelblue2', relief='raised')
canvas1.pack()

frame = tk.Frame(root, bg='lightsteelblue2')
frame.place(relwidth=1, relheight=1)
label1 = tk.Label(frame, text='Input string: ', bg='lightsteelblue2', font='20')
label1.place(x=10, y=10)
result_label = tk.Label(frame, text='', bg='lightsteelblue2', font='20')
entry1 = tk.Entry(frame, bg='lightsteelblue3', fg='black', font='30')
entry1.place(x=120, y=10, relwidth=0.3)
button1 = tk.Button(frame, text='Enter data', command=recBook,  bg='lightsteelblue1', fg='black', font=('helvetica', 12, 'bold'))
button1.place(x=10, y=50)
root.mainloop()
