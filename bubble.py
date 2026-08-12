n = int(input("Enter Number of Employees in a Company = "))

member = []

for i in range(n):
    salary = float(input("Member salary = "))
    member.append(salary)

print("Member Salary list (unsorted) =", member)

# Bubble Sort
for i in range(len(member) - 1):
    for j in range(len(member) - 1 - i):
        if member[j] > member[j + 1]:
            member[j], member[j + 1] = member[j + 1], member[j]

print("Sorted Member Salary list =", member)
