def binary_search(arr, target):
    lo, hi = 0, len(arr)-1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target: lo = mid + 1
        elif arr[mid] > target: hi = mid - 1
        else: return True
        
    return False

print( binary_search([1,2,3,4,5,6,7], 3) ) # True
print( binary_search([1,2,3,4,5,6,7], 0) ) # False