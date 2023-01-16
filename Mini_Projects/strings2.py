#   q               1
#         01234567890123
parrot = "Norwegian Blue"

print(parrot)
print(parrot[3])
# [3] is an index. it will print the 4th letter in the variable
# programming languages usually start programming from 0 rather than one
print()

print(parrot[3])    #w
print(parrot[4])    #e
print(parrot[9])
print(parrot[3])    #w
print(parrot[6])    #i
print(parrot[8])    #n

#but you can also use negative indexing to go backwards
print()

print(parrot[-11])    #w
print(parrot[-10])    #e
print(parrot[-5])
print(parrot[-11])    #w
print(parrot[-8])    #i
print(parrot[-6])

#notice how, to obtain the negative index values,
# you subtract the total string length from the positive index values

print()

print(parrot[3 - 14])    #w
print(parrot[4 - 14])    #e
print(parrot[9 - 14])
print(parrot[3 - 14])    #w
print(parrot[6 - 14])    #i
print(parrot[8 - 14])    #n

#                   1
#         01234567890123
parrot = "Norwegian Blue"

print()

#now we are going to begin slicing

print(parrot[0:6])  #Norweg
# [0:6] means including th zero character UP TO, NOT INCLUDING, the sixth
# so technially the 1st to the 5th
print(parrot[3:5])  #we
print(parrot[0:9])  #Norwegian
print(parrot[:9])   #Norwegian
#the two above are exactly the same, if you dont put the
# start index, automartically assumes the first character

print()

# the same applies for stop values

print(parrot[10:14])    #Blue
print(parrot[10:])    #Blue
# no stop value and it will automatically go to the end

print()

#so.....

print(parrot[:6] + parrot[6:])  #Norwegian Blue
print(parrot[:])  #Norwegian Blue

#You can also do indexes with negative values

print(parrot[-4:-2])    #Bl
print(parrot[-4:12])    #Bl

print()

#                   1
#         01234567890123
parrot = "Norwegian Blue"

print(parrot[0:6:2])    #Nre
#print 'parrot', from 0 up to, not inclding 6th index, every other 2 characters; steps of 2
print(parrot[0:6:3])    #Nw
#print 'parrot', from 0 up to, not inclding 6th index, every other 3 characters; steps of 3

print()

number = "9,193,574,197,571,609,887"
print(number[1::4])
# it prints, beginning with the first comma (the 9 is the zero'th index)
#every other 4th character, as indiciated by the  3rd step value

# should appear as
#,,,,,,