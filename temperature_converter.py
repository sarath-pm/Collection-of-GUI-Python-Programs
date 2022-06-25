'''
Requirements

# pip install tk

'''

import tkinter as tk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def convert_temp():
    if lbl_left['text']=='\N{DEGREE FAHRENHEIT}':
        temp_f = ent_temp.get()
        temp_c= (float(temp_f)-32)*5/9
        lbl_temp['text']=f"{round(temp_c, 2)}"
    else:
        temp_c = ent_temp.get()
        temp_f= (float(temp_c)*9/5)+32
        lbl_temp['text']=f"{round(temp_f, 2)}"        

def reverse():
    if lbl_left['text']=='\N{DEGREE FAHRENHEIT}':
        lbl_left['text']="\N{DEGREE CELSIUS}"
        lbl_right['text']='\N{DEGREE FAHRENHEIT}'
    else:
        lbl_left['text']='\N{DEGREE FAHRENHEIT}'
        lbl_right['text']='\N{DEGREE CELSIUS}'
        


window = tk.Tk()
window.title('Temperature Converter')

ent_temp = tk.Entry(master = window)
ent_temp.pack(side=tk.LEFT)
ent_temp.insert(0,'0')



lbl_left = tk.Label(text='\N{DEGREE FAHRENHEIT}', width=5)
lbl_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

btn = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}", command=convert_temp)
btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

lbl_temp = tk.Label(text='', width=10)
lbl_temp.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

lbl_right = tk.Label(text="\N{DEGREE CELSIUS}")
lbl_right.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)

btn_reverse = tk.Button(text='\N{CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS}', command=reverse)
btn_reverse.pack(side=tk.LEFT,fill=tk.BOTH, padx=6, expand=True)

window.mainloop()