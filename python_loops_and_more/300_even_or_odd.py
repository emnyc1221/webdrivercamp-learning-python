#!/usr/bin/python3
import random
random_num = random.randint(-10000, 10000)
last_digit = random_num % 10
even_status = "even" if last_digit % 2 == 0 else "odd"
if last_digit == 0:
    print(f"{random_num} - the last digit {last_digit} is zero")
else:
    print(f"{random_num} - the last digit {last_digit} is {even_status}")
