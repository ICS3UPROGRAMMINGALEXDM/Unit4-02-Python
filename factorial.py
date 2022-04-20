#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Uses a do-while loop to calculate factorial of a number entered
# by the user


def main():
    # initializing variables
    loop_count = 0
    factorial = 1

    u_num = input("Enter a number to be factorialized: ")

    try:
        num_int = int(u_num)
        # only calculate if number is in whole dataset
        if num_int >= 0:
            while True:
                # updating the loop count
                loop_count += 1
                print("{} times through loop".format(loop_count))
                # updating factorial
                factorial = factorial * loop_count
                # break when the loop count is greater or equal to the
                if loop_count >= num_int:
                    break

            print("The factorial of {0} is {1}".format(num_int, factorial))
        else:
            print("Number can not be negative")
    except ValueError:
        print("Invalid Input.")


if __name__ == "__main__":
    main()
