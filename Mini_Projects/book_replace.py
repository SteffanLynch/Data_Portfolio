# import os

# with open("/Users/steffanlynch/Desktop/Apprenticeship/Work_Based_Project/book.txt", "r") as input:
#     with open("temp.txt", "w") as output:
#         # iterate all lines from file
#         for line in input:
#             # if text matches then don't write it
#             if not line.strip("\n").contains('Highlight'):
#                 output.write(line)

# # replace file with original name
# os.replace('temp.txt', '/Users/steffanlynch/Desktop/Apprenticeship/Work_Based_Project/book.txt')


bad_words = ['Highlight', 'Location']

with open('/Users/steffanlynch/Desktop/Apprenticeship/Work_Based_Project/book.txt') as oldfile, open('newfile.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
            newfile.write('\n')