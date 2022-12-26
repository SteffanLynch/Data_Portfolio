shopping_list = ["milk", "eggs", "bread", "baked beans", "orange juice", "pasta"]

for item in shopping_list:
    if item == "pasta":
        continue

    print(item)

print("")
print("-------------------------------------------------")
print("")

item_to_find = "orange juice"
found_at = None
#for index in range (6)
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
#the below code is the exact same process and outcome as above.

#if item_to_find is in shopping_list:
#   found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))