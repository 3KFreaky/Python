#copyright Archer Hanrahan 2017

#This work is licensed under the Creative Commons Attribution 4.0 International
#License. To view a copy of this license,
#visit http://creativecommons.org/licenses/by/4.0/ or send a letter
#to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
#Steven Should Die
import tkinter
top = tkinter.Tk()
top.title("Click A Button!")
import random


def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def compliment():
    compliment = random.randint(1,9)

    if compliment == 1:
        print("Your Beautiful!")
    elif compliment == 2:
        print("Your Smile is Amazing!")
    elif compliment == 3:
        print("You look great today!")
    elif compliment == 4:
        print("You're a smart cookie!")
    elif compliment == 5:
        print("I like your style!")
    elif compliment == 6:
        print("You are the most perfect you there is!")
    elif compliment == 7:
        print("You're an awesome friend!")
    elif compliment == 8:
        print("You light up the room!")
    elif compliment == 9:
        print("You're all that and a super-size bag of chips!")

def insult():
    insult = random.randint(1,9)

    if insult == 1:
        print("You’re a good example of why some animals eat their young.")
    elif insult == 2:
        print("I didn’t attend Your funeral, but I sent a nice letter saying I approved of it.")
    elif insult == 3:
        print("I thought men like you shot themselves.")
    elif insult == 4:
        print("I can’t believe that out of 100,000 sperm, you were the quickest.")
    elif insult == 5:
        print("I like your style! where did you steal it?")
    elif insult == 6:
        print("We all have to wait in line to hate you.")
    elif insult == 7:
        print("You seem to have descended from the chimpanzee later than everyone else")
    elif insult == 8:
        print("You must have been born on a highway, because that's where most accidents happen.")
    elif insult == 9:
        print("You're so ugly Hello Kitty said goodbye to you.")

def THECODE():
    count = 0
    while count != 1:
        print("739823748923748923743289472389472389472347398237489237489237432894723894723894723473982374892374892374328947238947238947234739823748923748923743289472389472")
        print("347234732894823904848239048239048239482393472347328948239048482390482390482394823934723473289482390484823904823904823948239347234732894823904848239048239048")
        print("739823748923748923743289472389472389472347398237489237489237432894723894723894723473982374892374892374328947238947238947234739823748923748923743289472389472")
        print("483290483258464303485349493490593405934054832904832584643034853494934905934059340548329048325846430348534949349059340593405483290483258464303485349493490593")
        print("347234732894823904848239048239048239482393472347328948239048482390482390482394823934723473289482390484823904823904823948239347234732894823904848239048239048")
        
A = tkinter.Button(top, text ="Compliment", command = compliment)
B = tkinter.Button(top, text="CLEAR", command = clear)
C = tkinter.Button(top, text ="Insult", command = insult)
D = tkinter.Button(top, text = "THE CODE", command = THECODE)


A.pack()
C.pack()
D.pack()
B.pack()

top.mainloop()

#copyright Archer Hanrahan 2017












