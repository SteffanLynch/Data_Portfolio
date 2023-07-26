option1 = "1:\tGo Swimming"
option2 = "2.\tDo a workout"
option3 = "3.\tHave Good Sex"
option4 = "4.\tWatch a Film"
option5 = "5.\tRead Your Bible"
option6 = "6.\tGo on Holiday"
option7 = "0.\tExit"

menu = [option1, option2, option3, option4, option5, option6]
print(option1)
print(option2)
print(option3)
print(option4)
print(option5)
print(option6)




while True:
    choice = input(print("Choose a number frpm the list: "))

    if choice == "0":
        break

    elif choice in "123456":
            print("You chose option {}".format(choice))

    print("")

