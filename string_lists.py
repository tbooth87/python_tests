# Ask the user for a string and print whether or not it's a palindrome
# palindrome is a string that reads the same forwards and backwards

def is_palindrome(str_in):
    # Reverse the string that we get in
    str_tmp = ""
    i = len(str_in) - 1
    while i >= 0:
        str_tmp += str_in[i]
        i = i - 1

    # Compare the IN string with the reversed one
    if str_in.lower() == str_tmp.lower():
        return True
    else:
        return False

user_str = input("Enter a string: ")

ret = is_palindrome(user_str)

# Print the results
if ret is True:
    print(user_str + " is a palindrome!")
else:
    print(user_str + " is NOT a palindrome!")
