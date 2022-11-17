# Interview Question #3
#
# Our task is to design an efficient algorithm to reverse a given integer.
# For example if the input of the algorithm is 1234 then the output should be 4321.



print("my code")

# in this program I treated the number as a string, so I could conduct the slicing operation


def reverse_integer(integer):
    reverse_integer = integer[::-1]
    return reverse_integer

# here I considered the number as a string
number = input("Enter a number")
print(reverse_integer(number))



