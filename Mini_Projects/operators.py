a = 12
b = 3

#An expression is an instruction that combines values
# and operators and always has to be evaluated to a single value

print(a + b)    #15
print(a - b)    #9
print(a * b)    #36
print(a / b)    #4.0
#when you divide, the answer will be a float type
print(a // b)   #4
#to make the answer an integer type, you much use double //
print(a % b)    #0
# remainder operator used to find the remaining value after division

print()

for i in range(1, a // b): #lool dont forget the colon lool
    #range function can only use integer values so use division integer //
    print(i)

#for loop is essentiall doing as follows...
i = 1
print(i)
i = 2
print(i)
i = 3
print(i)


print(a + b / 3 - 4 * 12)  #-35.0
#we didnt use operator precedence. very similar to bidmas
print(a + (b / 3) - (4 * 12))
#in essence, that is what the code evalutated
#below is what we WANT
print((((a + b) /3) - 4) * 12)
#
print(((a + b) /3 - 4) * 12)