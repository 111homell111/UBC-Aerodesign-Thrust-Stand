from openpyxl import Workbook
from openpyxl import load_workbook
import os
from datetime import datetime

first = 0
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

wb = load_workbook(filename = (os.path.join(__location__, 'Test_data')+'.xlsx'))
ws = wb['Manual']
#current_row = ws.max_row + 1
 
#thrusts = []

for i in range (9): #Thrust
    
    if first == 0:
        ws.append([datetime.today().strftime('%Y-%m-%d %H:%M:%S')])
        first = 1

    throttle = i
    thrust = i+1
    current = 999999

    ws.append([throttle, thrust, current])  

    wb.save(filename=os.path.join(__location__, 'Test_data')+'.xlsx')
    wb.close()
