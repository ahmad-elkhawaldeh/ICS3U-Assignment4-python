# !/usr/bin/env python3

# created by: Ahmad El-khawaldeh
# created on: Nov 2020
# This program will get
# This program Takes two values from user and print greatest among them


def main():

    # Input
    value1 = print(" Please Enter the First Value ")
    value2 = print(" Please Enter the Second Value ")

    value1_string = input("Enter value1 integer: ")
    value2_string = input("Enter value2 integer: ")
    # process/output
    try:
        value1 = int(value1_string)
        value2 = int(value2_string)

        if(value1 > value2):
            print("{0} is Greater than {1}".format(value1, value2))
        elif(value2 > value1):
            print("{0} is Greater than {1}".format(value2, value1))
        else:
            print("Both a and b are Equal")

    except Exception:
        print("This was an invalid number ")


if __name__ == "__main__":
    main()
