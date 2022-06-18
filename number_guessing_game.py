'''
Requirements

# pip install tk
'''

# import necessary py modules
import tkinter as tk
from random import randrange

# Creating GUI 
window = tk.Tk()
window.title("Number Guessing Game")

lblInst = tk.Label(window, text = "Guess a number from 0 to 9")
lblLine0 = tk.Label(window, text = "*********************************************************************")
lblNoGuess = tk.Label(window, text = "No of Guesses: 0")
lblMaxGuess = tk.Label(window, text = "Max Guess: 3")
lblLine1 = tk.Label(window, text = "*********************************************************************")
lblLogs = tk.Label(window, text="Game Logs")
lblLine2 = tk.Label(window, text = "*********************************************************************")

# create the buttons
buttons = []
for index in range(0, 10):
    button = tk.Button(window, text=index, command=lambda index=index : process(index), state=tk.DISABLED)
    buttons.append(button)


btnStartGameList = []
for index in range(0, 1):
    btnStartGame = tk.Button(window, text="Start Game", command=lambda : startgame(index))
    btnStartGameList.append(btnStartGame)

# append elements to grid
lblInst.grid(row=0, column=0, columnspan=5)
lblLine0.grid(row=1, column=0, columnspan=5)
lblNoGuess.grid(row=2, column=0, columnspan=3)
lblMaxGuess.grid(row=2, column=3, columnspan=2)
lblLine1.grid(row=3, column=0, columnspan=5)
lblLogs.grid(row=4, column=0, columnspan=5)  # row 4 - 8 is reserved for showing logs
lblLine2.grid(row=9, column=0, columnspan=5)


for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
        buttons[i].grid(row=row+10, column=col)

btnStartGameList[0].grid(row=13, column=0, columnspan=5)

# Main game logic
guess = 0
totalNumberOfGuesses = 0
secretNumber = randrange(10)
print(secretNumber)
lblLogs = []
guess_row = 4

# reset all variables
def init():
    global buttons, guess, totalNumberOfGuesses, secretNumber, lblNoGuess, lblLogs, guess_row
    guess = 0
    totalNumberOfGuesses = 0
    secretNumber = randrange(10)
    print(secretNumber)
    lblNoGuess["text"] = "Number of Guesses: 0"
    guess_row = 4

    # remove all logs on init
    for lblLog in lblLogs:
        lblLog.grid_forget()
    lblLogs = []


def process(i):
    global totalNumberOfGuesses, buttons, guess_row
    guess = i

    totalNumberOfGuesses += 1
    lblNoGuess["text"] = "Number of Guesses: " + str(totalNumberOfGuesses)

    # check if guess match secret number
    if guess == secretNumber:
        lbl = tk.Label(window, text="Your guess was right. You won! :) ", fg="green")
        lbl.grid(row=guess_row, column=0, columnspan=5)
        lblLogs.append(lbl)
        guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED
    else:
        # give player some hints
        if guess > secretNumber:
            lbl = tk.Label(window, text="Secret number is less than your current guess :)", fg="red")
            lbl.grid(row=guess_row, column=0, columnspan=5)
            lblLogs.append(lbl)
            guess_row += 1
        else:
            lbl = tk.Label(window, text="Secret number is greater than your current guess :)", fg="red")
            lbl.grid(row=guess_row, column=0, columnspan=5)
            lblLogs.append(lbl)
            guess_row += 1

    # game is over when max no of guesses is reached
    if totalNumberOfGuesses == 3:
        if guess != secretNumber:
            lbl = tk.Label(window, text="Max guesses reached. You lost! :)", fg="red")
            lbl.grid(row=guess_row, column=0, columnspan=5)
            lblLogs.append(lbl)
            guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED

    buttons[i]["state"] = tk.DISABLED


status = "none"


def startgame(i):
    global status
    for b in buttons:
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        btnStartGameList[i]["text"] = "Retart Game"
    else:
        status = "restarted"
        init()
    print("Game started")


window.mainloop()