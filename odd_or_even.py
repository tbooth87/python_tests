number = int(input("Please enter a number: "))

if number % 2 == 0:
    if number % 4 == 0:
        print("The number " + str(number) + " is a multiple of 4!")
    else:
        print("The number " + str(number) + " is even!")
else:
    print("The number " + str(number) + " is odd!")
