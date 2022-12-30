import random

global student_answer
global diff_input

number_of_good_answers = 0
diff_input = 0

"""
Ask for the level of difficulty
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
"""


def difficulty_choice():
    global diff_input
    validator = "WRONG"
    while validator != "OK":
        try:
            diff_input = int(input(
                "Which level do you want? Enter a number: \n 1 - simple operations with numbers 2-9\n 2 - integral "
                "squares of 11-29\n"))
            validator = "OK"
            return diff_input
        except (Exception, ValueError, TypeError, NameError):
            validator = "WRONG"
            print("Incorrect format")



"""
Generate the math tasks 1 or 2 and set variables
"""

operators = ["+", "-", "*"]
v1, v2, v3, oper = 0, 0, 0, ""
yes_directory = ["yes", "YES", "y", "Yes"]

def generate_task1():
    global v1, v2, oper
    random.seed()
    v1 = random.randint(2, 9)
    v2 = random.randint(2, 9)
    oper = random.choice(operators)
    print(f"{v1} {oper} {v2}")

def generate_task2():
    global v3
    random.seed()
    v3 = random.randint(11, 29)
    print(v3)



"""
Get the student input 
"""


def get_student_input():
    global student_answer

    # This is an input validator, checking that the Value, Type, and Name Errors are well handled
    validator = "WRONG"
    while validator != "OK":
        try:
            student_answer = int(input())
            validator = "OK"
            return student_answer
        except (Exception, ValueError, TypeError, NameError):
            validator = "WRONG"
            print("Incorrect format")


"""
Do the math
"""


def calculate(v1, oper, v2):
    if oper == "*":
        return v1 * v2
    elif oper == "+":
        return v1 + v2
    elif oper == "-":
        return v1 - v2
    else:
        print("wrong math operation")


"""
Evaluate and print evaluation result
"""


def eval_and_print():
    global number_of_good_answers
    if student_answer == comp_answer:
        number_of_good_answers = number_of_good_answers + 1
        print("Right")
    else:
        print("Wrong")


"""
Stats and Safe: After five tasks, output Your mark is n/5. where n is the number of correct answers and asks for saving
"""


def statistics():
    global yes_directory
    global diff_input
    saving_input = str(input(f"Your mark is {number_of_good_answers}/5. Would you like to save the result? Enter yes or no."))
    if saving_input in yes_directory:
        student_name = input("What is your name?")
        stat_file = open("results.txt", mode="a")
        if diff_input == 1:
            stat_file.writelines(f"{student_name}: {number_of_good_answers}/5 in level 1 (simple operations with numbers 2-9) \n")
            print("The results are saved in \"results.txt\"")
            stat_file.close()
        else:
            stat_file.write(f"{student_name}: {number_of_good_answers}/5 in level 2 (integral squares of 11-29)")
            print("The results are saved in \"results.txt\"")
            stat_file.close()
    else:
        pass




"""
5 cycles rum
"""

difficulty_choice()
i = 0
while i < 5:
    if diff_input == 1:
        generate_task1()
        get_student_input()
        comp_answer = calculate(v1, oper, v2)
        eval_and_print()
        i = i + 1
    else:
        generate_task2()
        get_student_input()
        comp_answer = pow(v3, 2)
        eval_and_print()
        i = i + 1
statistics()