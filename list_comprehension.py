# Given a list of numbers create a new list with only the even numbers

nums = [1, 4, 6, 7, 9, 23, 11, 66, 88]

# newList = []
# for n in nums:
#     if n % 2 == 0:
#         newList.append(n)

newList = [n for n in nums if n % 2 == 0]

print(newList)