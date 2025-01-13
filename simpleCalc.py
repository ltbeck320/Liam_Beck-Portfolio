#Liam Beck
#11/18
#pd.5

#calculator
#init

#functions
def add(num1,num2):
    sum = int(num1)+int(num2)
    print(num1+"+"+num2+"="+str(sum))
def minus(num1,num2):
    difference = int(num1)-int(num2)
    print(num1+"-"+num2+"="+str(difference))
def times(num1,num2):
    product = int(num1)*int(num2)
    print(num1+"*"+num2+"="+str(product))
def over(num1,num2):
    Q = int(num1)/int(num2)
    print(num1+"/"+num2+"="+str(Q))
def calc():
    print("welcome to the simple calculator")
    while True:
        print("please choose an available operation, or type quit to stop the calculator")
        ope=input("operation: ")
        if ope == "add" or ope == "Add" or ope == "+" or ope == "addition" or ope == "Addition" or ope == "plus" or ope == "Plus":
            numone = input("choose your first number: ")
            numtwo = input("choose your second number: ")
            add(numone,numtwo)
        if ope == "subtract" or ope == "Subtract" or ope == "-" or ope == "subtraction" or ope == "Subtraction" or ope == "minus" or ope == "Minus":
            numone = input("choose your first number: ")
            numtwo = input("choose your second number: ")
            minus(numone,numtwo)
        if ope == "multiply" or ope == "Multiply" or ope == "*" or ope == "multiplication" or ope == "Multiplication" or ope == "times" or ope == "Times" or ope == "x" or ope == "by" or ope == "By":
            numone = input("choose your first number: ")
            numtwo = input("choose your second number: ")
            times(numone,numtwo)
        if ope == "divide" or ope == "Divide" or ope == "/" or ope == "division" or ope == "Division" or ope == "over" or ope == "Over":
            numone = input("choose your first number: ")
            numtwo = input("choose your second number: ")
            over(numone,numtwo)
        if ope == "quit" or ope == "stop" or ope == "Quit" or ope == "Stop":
            break
#main
calc()
