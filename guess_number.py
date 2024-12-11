# import randint from random module for generating number
from random import randint

# function to get the starting and ending range to generate number and return the number
def get_num():
    while True:
        try:
            min_num = int(input("Whats the starting range? "))
            max_num = int(input("What the end of range? "))
            if min_num >= max_num:
                print("The starting range must be less that ending range.")
            else:
                return randint(min_num, max_num)
        except ValueError:
            print("Please enter number.")

right_num = get_num()
count = 0
# loops for user input int before user get the right number. tracks the attempts user took
while True:
    try:
        user_num = int(input("Try to guess the number: "))
        if user_num == right_num:
            count += 1
            print("You Win!","\n",f"It took you {count} attempts.")
            print()
            break
        elif user_num > right_num:
            print("Too High :(")
            count += 1
        else:
            print("Too Low :(")
            count += 1
    except ValueError:
        count += 1
        print("Please enter number.")