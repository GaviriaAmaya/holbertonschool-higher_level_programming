#!/usr/bin/python3
"Take a random number and defines the last number"
import random
number = random.randint(-10000, 10000)
"Absolute value of number, to take the right module"
if number < 0:
    module = ((number * -1) % 10) * -1
else:
    module = number % 10
print("Last digit of {:d} is {:d} ".format(number, module), end="")

if module > 5:
    print("and is greater than 5")
elif module == 0:
    print("and is 0")
elif module < 6 and module != 0:
    print("and is less than 6 and not 0")
