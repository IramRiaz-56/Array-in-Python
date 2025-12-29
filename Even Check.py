# Python Program
# To Check and Display Even Number In Araay


def insertion(arr, size):   #Function to insert values in array
    for i in range(size):
        val = int(input(f"Enter Element {i+1}: "))
        arr.append(val)
        print(f"{val} inserted in Array.")
def display(arr):     #Function to display array
    print("Current array:", arr)
def even(arr):  #Function to return list of even numbers  
    even_nums = []
    for val in arr:
        if val % 2 == 0:
            even_nums.append(val)
    return even_nums
def displayEven(even_nums):        #Function to display even numbers
    print("Even numbers in array:", even_nums)


arr = []
size = int(input("How many values do you want to enter in the array? "))
insertion(arr, size)
display(arr)
even_nums = even(arr)         # Get even numbers
displayEven(even_nums)        # Display even numbers
