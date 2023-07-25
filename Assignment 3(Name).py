from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(bg='white',height=350,width=300)
canvas.create_rectangle(50, 60, 240, 160, fill='yellow', outline='blue')
canvas.create_text(100, 100, text='Lewis', anchor='nw', font='TkMenuFont', fill='black')
canvas.create_line(100, 115, 130, 115)
canvas.pack()
frame.mainloop()
