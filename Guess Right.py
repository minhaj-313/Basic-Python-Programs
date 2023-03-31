import random
n = random.randint(1,50)

while(True):
    inp = int(input())
    if(inp<n):
        print("Wrong guess, try a greator number")
    elif(inp>n):
        print("wrong guess, try a smaller number")
    else:
        print("Congratulations, You have guess the number")
        break;
