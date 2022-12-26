for i in range(1, 21):
    print("i is now {}".format(i))

print("")

print("-" * 80)

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} x {1} = {2}".format(i, j, i * j))
    print("--------------------")