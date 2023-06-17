import random
a=[]
n=int(input())
for i in range (n):
    a.append(random.randint(0,200))
for i in range(1,n):
    key=a[i]
    j=i-1
    
    while j>=0 and key<a[j]:
        a[j],a[j+1]=a[j+1],a[j]
        j=j-1
    
print(a)