import random
import time

OPERATORS = ["+", "-", "*"] #uses only the operators "(+,-,*)"
MIN_OPERAND = 1             #minimum operand will be 1
MAX_OPERAND = 10            #maximum operand will be 10
TOTAL_PROBLEMS = 10         #10 random problems will be presented

def generate_problem():     #will generate problem with random.randint operands on both left and right.
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right) #problem format
    answer = eval(expr)
    return expr, answer

wrong = 0
#instructs the player
print("                         ")
print(" Press enter to continue ")
input("                         ")
#introduces the game
print("*************************")
print("*                       *")
print("*----------THE----------*")
print("*-----MATH CHALLENGE----*")
print("*                       *")
input("*************************")
print("*-by: Mozar, Markeila V-*")
input("*************************")

print("                         ")
print("*************************")
print("*                       *")
print("------Are you ready?-----")
print("*                       *")
input("*************************")

print("                         ")
print("*************************")
print("*                       *")
print("*-Press enter to start!--")
print("*                       *")
input("*************************")

print("          *******        ")
print("          * !3! *        ")
input("          *******        ")
print("                         ")
print("          *******        ")
print("          * !2! *        ")
input("          *******        ")
print("                         ")
print("          *******        ")
print("          * !1! *        ")
input("          *******        ")
print("                         ")

print("First Question! Goodluck<3")

start_time = time.time()
#starts timer
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " =" " ")
        if guess == str(answer):
            print("              "),print("You did it! Next Question:>") 
            #shows when the player answers he question correctly and proceeds to the next question
            break
        
        wrong == 1
        print("              "),print("Not Quite! Try Again:<")
        #shows when the player incorrectly answers the question and repeats the problem until the player gets it right

end_time = time.time()
#ends timer
total_time = round(end_time - start_time, 2)

print("                         ")
print("*************************")
print("*                       *")
print("*    Yay you did it!    *")
print("*    You finished in    *")
print("*""    " , total_time, "seconds!""    " "*")
#displays the total amount of time it took the player to answer in seconds
print("*                       *")
input("*************************")

print("*************************")
print("                         ")
print("   You did your best<3   ")
print("     Until Next Time!    ")
print("          Bye<3          ")
print("                         ")
print("*************************")
print("                         ")

input("Do you want to try again?")
print("                         ")
print("Please Rerun Pyhton File")
print("                         ")
print("        Gwenchana!       ")