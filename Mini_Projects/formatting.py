for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}.".format(i, i ** 2, i ** 3))
    #very useful purpose for the replacement field
    #** means to the power of (the number following afterwards)

#as you see though, when printed, the values and text doesnt align
#so we can fix that by formatting and assing a width value to each replacement field

print()
print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}.".format(i, i ** 2, i ** 3))