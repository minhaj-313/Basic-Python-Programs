initial=int(input("Enter the lower limit number:"))
final=int(input("Enter the higher limit number:"))

sum=0
for i in range(initial,final+1):
    if i%2==0:
        sum+=i

print("The sum of even numbers from ",initial," to ",final,"is -> ",sum)