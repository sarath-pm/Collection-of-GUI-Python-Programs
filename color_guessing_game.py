'''
Requirements

# pip install tk
'''

# import necessary modules
import tkinter 
import random 

# predefinced variables
colours = ['Red','Blue','Green','Pink','Black', 'Yellow','Orange','White','Purple','Brown'] 
score = 0
timeleft = 30

# function to start game
def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour() 

# function to display next random color
def nextColour():
    global score 
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score)) 

# function for countdown timer
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: "+ str(timeleft))
        timeLabel.after(1000, countdown) 
        
windows = tkinter.Tk() 
windows.title("COLOR GAME") 
windows.geometry("375x200") 
instructions = tkinter.Label(windows, text = "Type in the colour of the words, and not the word text!",font = ('Helvetica', 12)) 
instructions.pack() 
scoreLabel = tkinter.Label(windows, text = "Press enter to start", font = ('Helvetica', 12)) 
scoreLabel.pack() 
timeLabel = tkinter.Label(windows, text = "Time left: " +str(timeleft), font = ('Helvetica', 12)) 				
timeLabel.pack() 
label = tkinter.Label(windows, font = ('Helvetica', 60)) 
label.pack() 
e = tkinter.Entry(windows) 
windows.bind('<Return>', startGame) 
e.pack() 
e.focus_set() 
windows.mainloop() 