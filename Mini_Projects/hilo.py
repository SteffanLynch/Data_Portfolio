low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
print("Press ENTER when ready to start")

guesses = 1
while low != high:
    print("\tGuessing in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2
    hi_lo = input("My guess is {}. Should I guess higher or lower? "
                  "Enter h if higher, l if lower or c if correct"

                  .format(guess)).casefold()
    if hi_lo == "h":
        # Guess higher. So the lowest value now becomes 1 higher than the guess
        low = guess + 1
    elif hi_lo == "l":
        # Guess lower. So the highest value now becomes 1 lower than the guess
        high = guess - 1
    elif hi_lo == "c":
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("Print only h, l or c")

    #guesses = guesses + 1
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I guessed your number in {} guesses".format(guesses))

    #this only works when the numbers (high and low) converge to the
    #number