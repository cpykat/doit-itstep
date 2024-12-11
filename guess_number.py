import random
from random import randint

def get_num():
    min_num = int(input("Whats the starting range? "))
    max_num = int(input("What the end of range? "))
    return randint(min_num,max_num)
right_num = get_num()

while True:
    user_num = int(input("Try to guess the number: "))
    if user_num == right_num:
        print("You Win!")
        break
    elif user_num > right_num:
        print("Too High :(")
    else:
        print("Too Low :(")