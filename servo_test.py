from tkinter import *
import serial

port = '/dev/cu.usbmodem11101' #port u can find on bottom right of arduino screen
baud_rate = 115200 #idk it just has to match on arduino code (this or 9600)
arduino = serial.Serial(port, baud_rate)

window = Tk() #creates the window
window.title("Servo Control") #window name
window.geometry("300x150") #initial window size?

def slider_changed(slider): #whenever the slider gets changed
    string = 'X{0:d}Y{1:d}'.format(slider_x.get(),slider_y.get()) #format it as like X100Y100 the numbers are slider.get() which gets the value of the slider
    #print(string)
    arduino.write(string.encode('utf-8')) #send the string to the arduino


slider_x = Scale(window, from_ = 0, to = 180, orient= 'horizontal', command = slider_changed, length = 200) #x slider
slider_y = Scale(window, from_ = 180, to = 0, orient = 'horizontal', command = slider_changed, length = 200) #y sk


slider_x.pack()
slider_y.pack()

window.bind("<Left>", lambda e: slider_x.set(slider_x.get()-10))
window.bind("<Right>", lambda e: slider_x.set(slider_x.get()+10))



window.mainloop()



'''
def myClick():
    IDK=Label(window,text="pebs")
    IDK.pack()

label = Label(window, text="Hello World!")
label.pack()

but = Button(window, text="click me", command=myClick)
but.pack()'''