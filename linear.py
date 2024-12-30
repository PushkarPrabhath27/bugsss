def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i    
    return -1  

arr = [3, 8, 1, 6, 10, 14]
target = 10
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
