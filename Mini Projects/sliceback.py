letters = "abcdefghijklmnopqrstuvwxyz"
#we want to print the alphabet backwards, so will slice backwards

backwards = letters[25:0:-1]
print(backwards)
#you see it only prints "zyxwvutsrqponmlkjihgfedcb"
#not including 'a', the stop value is UP TO the zero'th character, not including

backwards = letters[25::-1]
print(backwards)
#omitting the stop value will solve the issue
#so will omitting the start value...

backwards = letters[::-1]
print(backwards)

letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[16:13:-1]) #qpo
print(letters[4::-1]) #edcba
print(letters[:17:-1]) #zyxwvuts
