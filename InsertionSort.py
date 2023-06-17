import random
a=[]
n=int(input())
# Generating 200 random numbers to sort
for i in range (n):
    a.append(random.randint(0,200))


# Iterate from the second element to the last element in the list
for i in range(1, n):
    # Store the current element in the variable 'key'
    key = a[i]
    
    # Set the initial value for the comparison index 'j'
    j = i - 1
    
    # Compare 'key' with elements before it and shift them to the right
    # until the correct position for 'key' is found
    while j >= 0 and key < a[j]:
        # Swap elements a[j] and a[j+1]
        a[j], a[j+1] = a[j+1], a[j]
        
        # Decrement 'j' to compare 'key' with the previous element
        j = j - 1

# Print the sorted list
print(a)
