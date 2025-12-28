#Python Program
# Inout two Tabular Array & Sum them in Third Array

# #Set rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

#Initialize tables A and B
A = []
B = []

print("\nEnter values for Table A:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"A[{i}][{j}]: "))
        row.append(val)
    A.append(row)

print("\nEnter values for Table B:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"B[{i}][{j}]: "))
        row.append(val)
    B.append(row)

#Add A and B into C
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

#Function to display a table
def display_table(name, table):
    print(f"name:" , name)
    for row in table:
        print(row)

#Display all tables
display_table("A", A)
display_table("B", B)
display_table("C (A + B)" ,C )