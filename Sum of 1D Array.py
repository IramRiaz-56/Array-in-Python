#Python Program: Input Array & Sum Elements

#Take number of elements
n = int(input("Enter number of elements: "))

#Input elements from user
arr = []
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

#Calculate sum of elements
total = sum(arr)

#Display result
print("Array:", arr)
print("Sum of elements:", total)