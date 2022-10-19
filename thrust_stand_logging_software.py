'''
    Purpose: I hate APSC 160
    Purpose: Control thrust stand dfj;;lkafslkjfjdkla;fadf;jdsfj;ksfjk;la
'''



'''-----------------Import Libraries----------------'''
import tkinter as tk
from tkinter import ttk
import serial
import os

#Will need these bottom two imports to plot/display realtime data
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation


'''---------------Set Up Arduino -----------------'''
port = '/dev/cu.usbmodem11201' #You can find the port on the bottom right of
baud_rate = 115200 #Idk it just has to match the Arduino's code (Prolly use 115200 or 9600 for now)
#arduino = serial.Serial(port, baud_rate)



'''-------------------??? :D---------------------'''
FOLDER = '/Users/ellayan/EllaPG/UBCAeroDesign /GitHub/UBC-Aerodesign-Thrust-Stand'
FILELIST = [fname for fname in os.listdir(FOLDER) if fname.endswith('.txt')]
WINDOW_WIDTH = "1000"
WINDOW_HEIGHT = "800"
BUTTON_HEIGHT = 3
BUTTON_WIDTH = 10
MODES = ["Automatic", "Manual", "Timed"]


'''------The Real Stuff--------'''
class Thrust_Gui:
    def __init__(self, window):
        '''-------------Create Main Window-------------'''
        self.window = window 
        self.title = window.title("Thrust Stand Controller")
        self.size = window.geometry(WINDOW_WIDTH + "x" + WINDOW_HEIGHT)


        '''------------------Create Widgets-----------------'''
        self.file_menu = ttk.Combobox(window, values = FILELIST, state="readonly", width = BUTTON_WIDTH + 1,)
        self.mode_value = tk.StringVar(window)
        self.mode_value.set(MODES[0])
        self.select_mode = tk.OptionMenu(window, self.mode_value, *MODES, command = self.change_mode)
        self.manual_button = tk.Button(window, command = self.foo)
        self.motor_slider = tk.Scale(window, from_ = 0, to = 180, orient = 'vertical', command = self.slider, length = 200, label = "Motor")
        self.start_button = tk.Button(window, command = self.foo, text = "Start" )
        #self.STOP_button
        #self.input_button
        #self.output_button
        #self.auto
        #self.curve
        #self.runtime


        '''------------------Format Widgets-------------------'''
        self.start_button.config(width = BUTTON_WIDTH, height = BUTTON_HEIGHT)


        '''----------------Place Widgets-----------------'''
        self.select_mode.place(relx = 0.05, rely = 0.05)
        self.file_menu.place(relx = 0.05, rely = 0.3)
        self.motor_slider.place(relx = 0.40, rely = 0.3)
        self.start_button.place(relx = 0.05, rely = 0.15)


    '''-------------------Create Functions------------------'''
    def foo(self):
        pass

    def manual(self):
        pass 

    def change_mode(self, mode):
        #Unrelated by when do I use a switch statement over elif
        if mode == MODES[0]:
            self.file_menu["state"] = "readonly"
        elif mode == MODES[1]:
            self.file_menu["state"] = "disabled"
        elif mode == MODES[2]:
            self.file_menu["state"] = "disabled"
            
    def slider(self):
        string = 'X{0:d}Y{1:d}'.format(self.motor_slider.get())
        #arduino.write(string.encode('utf-8'))


'''------------------Run Code---------------'''
root = tk.Tk()
app = Thrust_Gui(root)
root.mainloop()



'''
window.bind("<Left>", lambda e: slider_x.set(slider_x.get()-10))
window.bind("<Right>", lambda e: slider_x.set(slider_x.get()+10))
'''


