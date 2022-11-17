print("tutor code")

def reversed_integer(number):
    reverse = 0
    while number > 0:
        remainder = number % 10
        number = number // 10
        reverse = reverse * 10 + remainder

    return reverse


if __name__ == "__main__":
    number = int(input("Enter a number"))
    print(reversed_integer(number))