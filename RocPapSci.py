#Liam Beck
#1/7
#pd.5

#init
import random
w=0
t=0
l=0
#functions
def RocPapSci():
    global w
    global t
    global l
    print("Welcome to Rock Paper Scissors")
    while True:
        move=input("Make your move: ")
        mine=random.randint(1,3)
        move=move.lower()
        if move =="rock":
            if mine==1:
                print("We both chose rock, so its a draw.")
                t=t+1
            elif mine==2:
                print("I chose paper, so I WIN!!!!")
                l=l+1
            elif mine==3:
                print("I chose scissors, so you win.")
                w=w+1
        elif move =="paper":
            if mine==2:
                print("We both chose paper, so its a draw.")
                t=t+1
            elif mine==3:
                print("I chose scissors, so I WIN!!!!")
                l=l+1
            elif mine==1:
                print("I chose rock, so you win.")
                w=w+1
        elif move =="scissors":
            if mine==3:
                print("We both chose scissors, so its a draw.")
                t=t+1
            elif mine==1:
                print("I chose rock, so I WIN!!!!")
                l=l+1
            elif mine==2:
                print("I chose paper, so you win.")
                w=w+1
        else:
            print("You either misspelled your answer or did not chose one of the options, so try again.")
        print("Your current recots is "+str(w)+" wins, "+str(l)+" losses, and "+str(t)+" draws.")
        restart=input("Would you like to quit of play again(quitting will erase your data)?")
        restart=restart.lower()
        if restart == "quit":
            break
#main
RocPapSci()

