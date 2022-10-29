'''
    Purpose: I hate APSC 160
    Purpose: Control thrust stand dfj;;lkafslkjfjdkla;fadf;jdsfj;ksfjk;la

'''



'''-----------------Import Libraries----------------'''
from curses import window
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import serial
import os
from openpyxl import Workbook
import time



#Will need these bottom two imports to plot/display realtime data
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation


'''---------------Set Up Arduino -----------------'''
port = '/dev/cu.usbmodem11201' #You can find the port on the bottom right of
baud_rate = 115200 #Idk it just has to match the Arduino's code (Prolly use 115200 or 9600 for now)
arduino = serial.Serial(port, baud_rate)



'''-------------------??? :D---------------------'''
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
INPUTLIST = [fname for fname in os.listdir(__location__) if fname.endswith('.txt')]
OUTPUTLIST = [fname for fname in os.listdir(__location__) if fname.endswith('.xlsx')]
WINDOW_WIDTH = "1000"
WINDOW_HEIGHT = "800"
BUTTON_HEIGHT = 3
BUTTON_WIDTH = 10
MODES = ["Automatic", "Manual", "Timed"]


'''------The Real Stuff--------'''
class Thrust_Gui:
    def __init__(self, window):
        self.mode = MODES[0]


        '''-------------Create Main Window-------------'''
        self.window = window 
        self.title = window.title("Thrust Stand Controller")
        self.size = window.geometry(WINDOW_WIDTH + "x" + WINDOW_HEIGHT)


        '''------------------Create Widgets-----------------'''
        self.file_menu = ttk.Combobox(window, values = INPUTLIST, state="readonly", width = BUTTON_WIDTH + 1,)
        self.output_menu = ttk.Combobox(window, values = OUTPUTLIST, state="readonly", width = BUTTON_WIDTH + 1,)

        self.mode_value = tk.StringVar(window)
        self.mode_value.set(self.mode)
        self.select_mode = tk.OptionMenu(window, self.mode_value, *MODES, command = self.change_mode)

        
        #self.manual_button = tk.Button(window, command = self.foo)
        self.start_button = tk.Button(window, command = self.start, text = "Start" )
        self.motor_slider = tk.Scale(window, from_ = 0, to = 180, orient = 'vertical', command = self.slider, length = 200, label = "Motor")
       
        #self.output_box = tk.Text(window, height = 5, width = 17, state = "disabled")
        #self.STOP_button
        #self.input_button
        #self.output_button
        #self.auto
        #self.curve
        #self.runtime

        self.window.bind("<Up>", lambda e: self.motor_slider.set(self.motor_slider.get()-10))
        self.window.bind("<Down>", lambda e: self.motor_slider.set(self.motor_slider.get()+10))
        


        '''------------------Format Widgets-------------------'''
        self.start_button.config(width = BUTTON_WIDTH, height = BUTTON_HEIGHT)


        '''----------------Place Widgets-----------------'''
        self.select_mode.place(relx = 0.05, rely = 0.05)
        self.file_menu.place(relx = 0.05, rely = 0.3)
        self.motor_slider.place(relx = 0.40, rely = 0.3)
        self.start_button.place(relx = 0.05, rely = 0.15)
        self.output_menu.place(relx = 0.05, rely = 0.35)
        #self.output_box.place(relx=0.05, rely = 0.4)




    '''-------------------Create Functions------------------'''
    def start(self):
        '''
        Run a series of start checks, if passed, run test
        '''

        if self.mode == 'Automatic':
            if self.file_menu.get() == '':
                tk.messagebox.showinfo (title = 'Error', message = 'No input file selected!', icon = 'warning')
                return 0
            input_file = open(os.path.join(__location__, self.file_menu.get()), 'r')
            input_list = [line .rstrip('\n') for line in input_file.readlines()]
            input_list.append("000000")


        for i in range (len(input_list)):
            line = input_list[i]
            duration = int(line[3:])
            throttle = int(line[:3])
            #self.output_box.insert(tk.END, 'Throttle:  {0:d}s, Duration: {1:d}%'.format(throttle, duration) GOD hates me
            self.window.after(duration * 1000, self.send_throttle(throttle))
            print(line)

                

        #recieve data from arduino
        #take like ??? data points and take the average


        #write
        

    def send_throttle(self, throttle):
        string = 'X{0:d}'.format(throttle)
        arduino.write(string.encode('utf-8'))

    def stop(self):
        '''
        Tell Arduino to turn thrust to zero
        '''
        string = 'X0'
        arduino.write(string.encode('utf-8'))
        


    def change_mode(self, new_mode):
        '''
        Should turn certain widgets on and off based on test mode
        '''

        if new_mode == MODES[0]:
            self.file_menu["state"] = "readonly"
        elif new_mode == MODES[1]:
            self.file_menu["state"] = "disabled"
        elif new_mode == MODES[2]:
            self.file_menu["state"] = "disabled"
        self.mode = new_mode
        
    def slider(self, throttle):
        throttle = int(throttle) #for slider LOL or like just in case ig :) i would prefer to just pass ints... should i>??????a number
        string = 'X{0:d}'.format(throttle)
        arduino.write(string.encode('utf-8'))

    def save(self):
        pass
        #write to file lmfaooooo

'''------------------Run Code---------------'''
root = tk.Tk()
app = Thrust_Gui(root)
root.mainloop()

string = 'X0'
arduino.write(string.encode('utf-8'))

'''
NOTES:
- Uh calibrate by doing 100% then 0% and wait for the beeps lolol
- The lag is caused by keyboard inputs :,)





left and right arrow key to control sldier

'''


'''
create a pop up window
    def save(self):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
        '''

'''
          if self.output_menu.get() == '':
                self.no_output_message = tk.messagebox.askquestion(title = 'Warning', message = 'No output file selected. Proceed anyway? (Will create a new file)', icon = 'info')
                if self.no_output_message == 'No':
                    return 0
                elif self.no_output_message == 'Yes':
                    output_name = simpledialog.askstring(title = 'File Name', message = 'Please name your file (omit.xlsx)')
                    #IDK?????? LMAOOOO
                    
'''


                #Unrelated by when do I use a switch statement over elif

