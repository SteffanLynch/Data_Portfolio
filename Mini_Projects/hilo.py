low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
print("Press ENTER when ready to start")

guesses = 1
while low != high:
    print("\tGuessing in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2
    # basically, it guesses the midpoint between the range. when you say higher or lower, the range changes.
    hi_lo = input("My guess is {}. Should I guess higher or lower? "
                  "Enter h if higher, l if lower or c if correct"

                  .format(guess)).casefold()
                    # this format method basically inserts those variables in the order they appear, rather than having to concatenate them seperately.
                    # it makes things easier and more dynamic
    if hi_lo == "h":
        # Guess higher. So the lowest value now becomes 1 higher than the guess
        low = guess + 1
    elif hi_lo == "l":
        # Guess lower. So the highest value now becomes 1 lower than the guess
        high = guess - 1
    elif hi_lo == "c":
        print("I got it in {} guesses".format(guesses))
        break
        # break is a keyword in python
        # this break means that it cuts/exits out of the loop. As its got the answer correct, there is no need to go through the loop again.
        # used particular in while loops as they have the potential to run infinitely and then crash the program
        # ^^^^ for example, while 1 = 1 or while True
    else:
        print("Print only h, l or c")

    #guesses = guesses + 1
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I guessed your number in {} guesses".format(guesses))

    #this only works when the numbers (high and low) converge to the number
