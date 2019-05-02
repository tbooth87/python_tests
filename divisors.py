# Ask the user for a number and print a list of all divisors of that number

# Ask user for a number
user_num = int(input("Enter a number: "))

# Create a list of numbers from 1 to one less than the number the user entered
listRange = range(1, user_num+1)

# Loop through the range and add numbers that the user number is divisible by to a new list
divisorList = []
for element in listRange:
    if user_num % element == 0:
        divisorList.insert(0, element)

print(divisorList)

