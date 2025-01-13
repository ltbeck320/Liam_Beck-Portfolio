#Liam Beck
#11/12
#pd.5

#init
import random
points=0
#function
def pickANumber():
    global points
    diff=int(input("what difficulty do you wanna play?(1-3) "))
    if diff==1:
        guessone=int(input("pick a number 1-10: "))
        guesstwo=int(input("pick a number 1-10: "))
        guessthree=int(input("pick a number 1-10: "))
        secretone=random.randint(1,10)
        if guessone==secretone or guesstwo==secretone or guessthree==secretone:
            print("you got it right, it was "+str(secretone))
            points=points+5
            print("you have "+str(points)+" points")
            ans=input("do you wanna play again(choosing not to will forfeit your "+str(points)+" points)?(y/n) ")
            if ans=="y":
                pickANumber()
        else:
            print("you got it wrong, the number was "+str(secretone))
            print("you have "+str(points)+" points")
            ans=input("do you wanna play again(choosing not to will forfeit your "+str(points)+" points)?(y/n) ")
            if ans=="y":
                pickANumber()
    if diff==2:
        guess=int(input("pick a number 1-10: "))
        secret=random.randint(1,10)
        if guess==secret:
            print("you got it right congrats")
            points=points+15
            print("you have "+str(points)+" points")
            ans=input("do you wanna play again(choosing not to will forfeit your "+str(points)+" points)?(y/n) ")
            if ans=="y":
                pickANumber()
        else:
            if guess>secret:
                print("you guessed too high, the number was "+str(secret))
                print("you have "+str(points)+" points")
                ans=input("do you wanna play again(choosing not to will forfeit your "+str(points)+" points)?(y/n) ")
                if ans=="y":
                    pickANumber()
            if guess<secret:
                print("too low, the number was "+str(secret))
                print("you have "+str(points)+" points")
                ans=input("do you wanna play again(choosing not to will forfeit your "+str(points)+" points)?(y/n) ")
                if ans=="y":
                    pickANumber()
    if diff==3:
        evilguess=int(input("pick a number 1-100: "))
        evilsecret=random.randint(1,100)
        if evilguess==evilsecret:
            print("you got it right congrats")
            points=points+150
            print("you have "+str(points)+" points")
            ans=input("do you wanna play again(choosing not to will forfeit your "+str(points)+" points)?(y/n) ")
            if ans=="y":
                pickANumber()
        else:
            if evilguess>evilsecret:
                print("you guessed too high, the number was "+str(evilsecret))
                print("you have "+str(points)+" points")
                ans=input("do you wanna play again(choosing not to will forfeit your "+str(points)+" points)?(y/n) ")
                if ans=="y":
                    pickANumber()
            if evilguess<evilsecret:
                print("too low, the number was "+str(evilsecret))
                print("you have "+str(points)+" points")
                ans=input("do you wanna play again(choosing not to will forfeit your "+str(points)+" points)?(y/n) ")
                if ans=="y":
                    pickANumber()


#main
pickANumber()

