# \ is a escape character and is used to negate the effect of whatever comes after it
space = " "


SplitString = "this string has\nbeen split\nover many\nlines because\nnewline escape\nwas used"
print(SplitString)
#\n is an escape character used for a new line.
print(space)
TabbedString = "This string\thas been\ttabbed\tbecause i\tdont know"
print(TabbedString)
#\t is a whitespace character that tabss the string (every 4 spaces I think)

print(space)

print("Naomi's dad said \"Come in for dinner\" and smiled")
#or
print('Naomi\'s dad said "Come in for dinner" and smiled')
#if you dont escape the apostrephe or speech marks,
# then it will consider it at the string for the function

#you can also use triple quotes at the beginning of a string an then
#you don't have to escape the characters because the function wont
# execute until it finds those 3 consecutive quotes again
print(space)

print("""Naomi's dad said "Come in for dinner" and smiled""")
#or
print("""Naomi's dad said 
"Come in for dinner" 
and smiled""")

#I can then use the backslash to negate the seperate lines

print("""Naomi's dad said \
"Come in for dinner" \
and smiled""")

print(r'your mum\nsmells\ncheese')
#in the above example, its not going to execute the newline escape
# because we prefixed the string with an 'r' for raw

