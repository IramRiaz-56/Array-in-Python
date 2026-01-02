#python program 
#Binary Search Program with Ascending Input Prompt


def binary_search(arr, target):          #Function to perform binary search
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid             #Target found
        elif arr[mid] < target:
            low = mid + 1            #Search in right half
        else:
            high = mid - 1        #Search in left half
    return -1                  #Target not found


arr = []
size = int(input("Enter number of elements (in ascending order): "))    # Input sorted array
for i in range(size):
    val = int(input(f"Enter element {i+1}: "))
    # Ensure ascending order
    if i > 0 and val < arr[i - 1]:
        print("Please enter values in ascending order!")
        break
    arr.append(val)
else:
    #Input target value
    target = int(input("Enter value to search: "))
    result = binary_search(arr, target)          # Perform binary search

    #Show result
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array.")
