import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0

print("                         ")
print(" Press enter to continue ")
input("                         ")

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

start_time = time.time()

print("First Question! Goodluck<3")

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + "=" " ")
        if guess == str(answer):
            print("              "),print("You did it! Next Question:>")
            break
        
        wrong == 1
        print("              "),print("Not Quite! Try Again:<")

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("                         ")
print("*************************")
print("*                       *")
print("*    Yay you did it!    *")
print("*    You finished in    *")
print("*""    " , total_time, "seconds!""    " "*")
print("*                       *")
input("*************************")

print("                         ")
print("        Gwenchana!       ")
print("          Bye<3          ")
print("                         ")
