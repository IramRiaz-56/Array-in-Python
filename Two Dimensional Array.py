# A simple Python program that:
#Takes user input into a table  
#Displays the table  
#Finds the largest and smallest* value in a numeric column (e.g., age or marks)

n = int(input("Enter number of records: "))   #Take number of record

table = []         #List to store table data

for i in range(n):      #Input data into the table
    print(f"\nEnter data for record {i+1}:")
    name = input("Name: ")
    marks = int(input("Marks: "))
    table.append([name, marks])

#Display table
print("\n--- Table ---")
print("{:<15} {:<10}".format("Name", "Marks"))
print("-" * 25)
for row in table:
    print("{:<15} {:<10}".format(row[0], row[1]))

marks_list = [row[1] for row in table] #Find max and min marks
max_val = max(marks_list)
min_val = min(marks_list)

print("\nHighest Marks:", max_val)
print("Lowest Marks:", min_val)