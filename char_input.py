import datetime

def is_valid_int(user_input):
    try:
        val = int(user_input)
    except:
        return False
    return True

# Given an age and future age, figure out what year it will be
# when they turn that age
def get_future_year(cur_age,future_age):
    # Get the current year
    cur_date = datetime.datetime.now()
    cur_year = cur_date.year

    # Get the number of years we need to add to the current year
    years_to_add = int(future_age) - int(cur_age)

    # Return
    return cur_year + years_to_add

name = input('What is your name? ')
age = input ('What is your age? ')

# Check that the age entered is a valid number
if is_valid_int(age) == True:
    # Get the current year
    new_year = get_future_year(age, 100)
    print("You will turn 100 in the year:" + str(new_year))

else:
    print('Please enter a valid age!')


# This is a change for a test commit






