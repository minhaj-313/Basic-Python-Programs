"""
    Convert a decimal number to a binary number
"""

try:
    decimal_num = int(input("Enter a decimal number: "))
    bin = 0
    ctr = 0
    tmp = decimal_num

except Exception as error:
    print("An error has occurred! => ", str(error))
    exit()

else:    
    while(tmp > 0):
        bin = ((tmp % 2) * (10 ** ctr)) + bin
        tmp = int(tmp / 2)
        ctr += 1 

    print("Binary of {x} is: {y}".format(x = decimal_num, y = bin))


