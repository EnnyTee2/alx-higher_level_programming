#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# the get_last function below gets the last digit of the number
def get_last(num):
    temp = str(num)
    last = int(temp[len(temp)-1])
    if num < 0:
        return last * -1
    return last
last_num = get_last(number)
if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
