from tkinter import *
import serial

port = '/dev/cu.usbmodem11301'
baud_rate = 115200
arduino = serial.Serial(port, baud_rate)

window = Tk()
window.title("Servo Control")
window.geometry("300x150")

def slider_changed(slider):
    string = 'X{0:d}Y{1:d}'.format(slider_x.get(),slider_y.get())
    arduino.write(string.encode('utf-8'))


slider_x = Scale(window, from_ = 0, to = 180, orient= 'horizontal', command = slider_changed, length = 200)
slider_y = Scale(window, from_ = 180, to = 0, orient = 'horizontal', command = slider_changed, length = 200)


slider_x.pack()
slider_y.pack()

window.bind("<Left>", lambda e: slider_x.set(slider_x.get()-30))
window.bind("<Right>", lambda e: slider_x.set(slider_x.get()+30))


window.mainloop()



'''
def myClick():
    IDK=Label(window,text="pebs")
    IDK.pack()

label = Label(window, text="Hello World!")
label.pack()

but = Button(window, text="click me", command=myClick)
but.pack()'''