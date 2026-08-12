n = int(input("Enter number of Emp's: "))

salary_list = []

print("-------------------------------------")

for i in range(n):
    salary = int(input("Enter salary (in thousands): "))
    salary_list.append(salary)

print("-------------------------------------")
print(salary_list)
print("-------------------------------------")

print("Now sort the list")
print("-------------------------------------")

# Bubble Sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        if salary_list[j] > salary_list[j + 1]:
            salary_list[j], salary_list[j + 1] = salary_list[j + 1], salary_list[j]

print("Sorted list:")
print(salary_list)