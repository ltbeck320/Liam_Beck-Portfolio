#Liam Beck
#1/9
#pd.5

#init
import random
#functions
def quiz():
    correct=0
    qnum=0
    print("Welcome to the Multiplication quiz.")
    diff=int(input("""What difficulty level would you like your quiz to be?
Please keep your answer as a number and note that the difficulty is exponential: """))
    questions=int(input("How many questions would you like to answer? "))
    start=input("To begin, type start: ")
    start=start.lower()
    if start=="start":
        for i in range(questions):
            qnum=qnum+1
            print("Question "+str(qnum)+" of "+str(questions)+":")
            num1=random.randint(10**(diff-1)+1,(10**diff)-1)
            num2=random.randint(10**(diff-1)+1,(10**diff)-1)
            numnum=num1*num2
            print("What is "+str(num1)+" * "+str(num2)+"?")
            ans=input("Your answer: ")
            if ans==str(numnum):
                correct=correct+1
                print("""Correct!

                      """)
            else:
                print("Sorry, the answer was "+str(numnum)+".")
                print("""
                      """)
        score=100*correct/questions
        print("You got "+str(correct)+" out of "+str(questions)+" questions correct, so your score is "+str(score)+" percent.")
#main
quiz()
