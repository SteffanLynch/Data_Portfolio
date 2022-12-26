import random

highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing

guess= int(input("Please guess a number between 1 and {}: ".format(highest)))
while guess != answer:
    if guess > answer:
        guess= int(input("Please guess a number lower: "))

    else:
        guess= int(input("Please guess a number higher: "))

if guess == answer:
    print("Well done you guessed it!!")