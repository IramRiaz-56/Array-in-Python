# One Dimensional Array
#Array Operations Program

def insertion(arr, size):               # Insert Element in Array
    for i in range(size):
     val = int(input(f"Enter Element{i+1}: "))
     arr.append(val)
     print(f"{val} inserted in Array.")

def insert_at_position(arr, pos, value):    # Insert Element at a Specific Position
    if 0 <= pos <= len(arr):
        arr.insert(pos, value)  # Insert at given index
        print(f"{value} inserted at position {pos}.")
    else:
        print("Invalid position!")

def insert_at_end(arr, value):            # Insert Element at the End
    arr.append(value)  # Append adds at end
    print(f"{value} inserted at end.")

def delete_at_position(arr, pos):    # Delete Element from a Specific Position
    if 0 <= pos < len(arr):
        removed = arr.pop(pos)  # Remove at index
        print(f"{removed} deleted from position {pos}.")
    else:
        print("Invalid position!")

def delete_at_end(arr):        # Delete element from the End
    if arr:
        removed = arr.pop()  # Removes last element
        print(f"{removed} deleted from end.")
    else:
        print("Array is empty!")
# Display the Current Array
def display(arr):
    print("Current array:", arr)

#--- Main Program ---
arr = []  # Initialize empty array (list)
while True:
    print("\n--- Array Operations Menu ---")
    print("1. Insert Elements in Array")
    print("2. Insert at Specific Position")
    print("3. Insert at End")
    print("4. Delete at Specific Position")
    print("5. Delete at End")
    print("6. Display Array")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        size = int(input("How many value you want to enter in Array"))
        insertion(arr, size)
    elif choice == '2':
        val = input("Enter value to insert: ")
        pos = int(input("Enter position (index): "))
        insert_at_position(arr, pos, val)
    elif choice == '3':
        val = input("Enter value to insert at end: ")
        insert_at_end(arr, val)
    elif choice == '4':
        pos = int(input("Enter position (index) to delete: "))
        delete_at_position(arr, pos)
    elif choice == '5':
        delete_at_end(arr)
    elif choice == '6':
        display(arr)
    elif choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again")






   