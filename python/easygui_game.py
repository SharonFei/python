import random,easygui
secert=random.randint(1,99)
guess=0
tries=0
easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts,and I have a secert!
It is a number from 1 to 99.I'll give you 6 tries.""")
while guess !=secert and tries <6:
    guess = easygui.integerbox("What's yer guess,matey?")
    if not guess:break
    if guess<secert:
        easygui.msgbox(str(guess)+"is too low,ye scurvy dog!")
    elif guess>secert:
        easygui.msgbox(str(guess)+"is too high,landlubber!")
    tries=tries+1
if guess==secert:
    easygui.msgbox("Avast!Ye got it ! Found my secert,ye did!")
else:
    easygui.msgbox("No more guesses! The number was "+str(secret))
