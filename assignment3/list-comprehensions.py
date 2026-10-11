import csv

# list of lists
with open("../csv/employees.csv", "r", newline="") as file:
    reader = csv.reader(file)
    employees = list(reader)

print(employees)

# names
employee_names = [row[1] + " " + row[2] for row in employees[1:]]
print(employee_names)

# e
names_with_e = [name for name in employee_names if "e" in name.lower()]
print(names_with_e)