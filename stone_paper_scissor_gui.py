'''
Requirements

# pip install tk
'''

# import necessary py modules
import random
import tkinter as tk
from PIL import Image,ImageTk
import requests

# open a window using tkinter
window=tk.Tk()
window.geometry("300x500")
window.title("Stone Paper Scissor")

# display an image in the application
image=Image.open(requests.get("https://i.pinimg.com/originals/f1/b3/09/f1b309ccb90c0a0a4911137503a3eeeb.jpg", stream=True).raw)
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=15,row=0)

#global variables
USER_SCORE=0
COMP_SCORE=0
USER_CHOICE=""
COMP_CHOICE=""


def choice_to_number(choice):
    rps={'scissor':0,'paper':1,'stone':2}
    return rps[choice]

def number_to_choice(number):
        rps={0:'scissor',1:'paper',2:'stone'}
        return rps[number]
    
def random_computer_choice():
    return random.choice(['scissor','paper','stone'])

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE

    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)

    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
         print("Sorry! Computer Wins!")
         USER_SCORE+=1
    else:
        print("Congarts! You win!")
        COMP_SCORE+=1
       

    # Text to display
    text_area=tk.Text(master=window,height=12,width=30)
    text_area.grid(column=15,row=4)
    answer="Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE, font=('arial',24,'bold'))
    text_area.insert(tk.END,answer)


# Event Handling 
def stone():
    global USER_CHOICE
    global COMP_CHOICE
    
    USER_CHOICE='stone'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
    
# buttons
button1=tk.Button(text="       Scissor         ",bg="light green",command=scissor, height=1,width=8,font=('arial',15,'bold'))
button1.grid(column=15,row=1)
button2=tk.Button(text="        Paper          ",bg="pink",command=paper, height=1,width=8,font=('arial',15,'bold'))
button2.grid(column=15,row=2)
button3=tk.Button(text="         Stone          ",bg="yellow",command=stone, height=1,width=8,font=('arial',15,'bold'))
button3.grid(column=15,row=3)  

window.mainloop()