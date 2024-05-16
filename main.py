import tkinter
import qrcode
from tkinter import *

display = Tk()
display.title('QR Code')
display.geometry('320x260')
display.resizable(False, False)


def do_qr():
    text = ready_text.get(0.1, tkinter.END)
    ready_text.delete(0.1, tkinter.END)
    img = qrcode.make(text)
    with open('db.txt', 'r+') as x:
        w1 = int(x.read())
        w1 += 1
        x.seek(0)
        x.write(str(w1))
        img.save('qrcode_{}.png'.format(int(w1)))
        print('Successfully, qrcode_{}.png created✔️'.format(int(w1)))


label = Label(display, text='Enter Text to Create QR Code')
label.place(x=0, y=0)

label2 = Label(display, text='Output:')
label2.place(x=320, y=20)

ready_text = Text(display)
ready_text.place(x=10, y=20, height=200, width=300)

submit = Button(display, text='Submit', command=do_qr)
submit.place(x=40, y=225, width=200)

exit1 = Button(display, text='Exit', command=exit)
exit1.place(x=270, y=225)

display.mainloop()
