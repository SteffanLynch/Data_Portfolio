age = 24
print("My age is " + str(age) + " years")
#in order to concatenate an integer value and coerce it into a string, you must
#include it a string function

#to make things easier though, you can use replacement fields, using the.format method
print("My age is {0} years".format(age))

print()

#the replacement field is represented by the {0}, which will be replaced by
#the first value in the format list

print("there are {0} letters in {1}, {2}, {3} and {4}"
      .format(7, "Steffan", "Kristan", "Malachi", "Herbert"))
print("there are {0} letters in Steffan, Kristan, Malachi and Herbert".format(7))
#they will equal the same thing. Just to demonstrate replacement fields
#however, they dont have to be in the same or any particular order

print()

print("Steffan: {0}, Kristan: {0}, Olivia: {1}, Malachi: {0}, Sharon: {1}, Herbert: {0}, Peter: {2}"
      .format(7, 6, 5))
print("""
Steffan:    {0}
Kristan:    {0} 
Olivia:     {1}
Malachi:    {0}
Sharon:     {1}
Herbert:    {0}
Peter:      {2}""".format(7, 6, 5))
#Replacement Field {0} = 7
#Replacement Field {1} = 6
#Replacement Field {2} = 5

