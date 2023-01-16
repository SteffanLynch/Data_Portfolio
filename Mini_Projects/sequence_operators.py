string1 = "Steffan "
string2 = "is a "
string3 = "strong man "
string4 = "when given "
string5 = "steroids"

print(string1 + string2 + string3 + string4 + string5)
print("Steffan " "is a " "strong man " "when given " "steroids")

print()

print(string1 * 5)
print("Steffan " * 5)

print()

print(string1 * (5 + 4))
print(string1 * 5 + "4")

print()

name = "Steffan"

print("Steff" in name)      #true
print("fan" in name)        #true
print("hello" in name)      #false
print("Steffam" in string2) #false

#the 'in' operator evaluates to true if the first thing exists in the second

