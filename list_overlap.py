# Create two lists, compare them and return a list that contains common values between them

import random

# Generate two random lists lengths
listLen1 = random.randint(1, 50)
listLen2 = random.randint(1, 50)

# Generate two lists of random numbers
myList1 = [random.randint(1, 50) for i in range(listLen1)]
myList2 = [random.randint(1, 50) for i in range(listLen2)]

# Sort the lists for readability
myList1.sort()
myList2.sort()
print(myList1)
print(myList2)

# Loop through the lists and create a new list with only common values between the two
# commonList = []
# for element in myList1:
#     if element in myList2 and element not in commonList:
#         commonList.append(element)

commonList = [n for n in myList1 if n in myList2]

print(commonList)
