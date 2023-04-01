"""
    Find the sum of all odd numbers in a given range
"""

try:
    max    = int(input("Enter the maximum value: "))
    Oddsum = 0

except Exception as error:
    print("An error has occurred! => ", str(error))
    exit()

else:
    for num in range(1, max + 1):
        if num % 2 != 0:
            print("{0}".format(num))
            Oddsum += num

    print("The sum of odd numbers from 1 to {0} = {1}".format(num, Oddsum))

