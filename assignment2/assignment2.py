import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 2
def read_employees():
    employees_dict = {}
    rows = []
    try:
        with open ('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            first = True
            for row in reader:
                if first:
                    employees_dict["fields"] = row
                    first = False
                else:
                    rows.append(row)
            employees_dict["rows"] = rows
            
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()
    return employees_dict
employees = read_employees()
print(employees)

# task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# task 4
def first_name(row_number):
    first_name_column = column_index("first_name")
    value = employees["rows"][row_number][first_name_column]
    return value

# task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

# task 6
def employee_find_2(employee_id):
    matches = list(filter(
        lambda row: int(row[employee_id_column]) == employee_id,
        employees["rows"]
    ))
    return matches

# task 7 
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

sort_by_last_name()
print(employees)

# task 8
def employee_dict(row):
    employee = {}

    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee[field] = row[i]

    return employee

print(employee_dict(employees["rows"][0]))

# task 9
# Task 9

def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees

print(all_employees_dict())

# task 10
def get_this_value():
    return os.getenv("THISVALUE")

# task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("abc")
print(custom_module.secret)

# task 12

def read_minutes():

    def read_file(filename):
        minutes = {}
        rows = []

        with open(filename, "r") as file:
            reader = csv.reader(file)
            first = True

            for row in reader:
                if first:
                    minutes["fields"] = row
                    first = False
                else:
                    rows.append(tuple(row))

            minutes["rows"] = rows

        return minutes

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

# task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    minutes_set = set1.union(set2)
    return minutes_set

minutes_set = create_minutes_set()
print(minutes_set)

# task 14

def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes_list))
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

# task 15
# Task 15

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list))
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list

write_sorted_list()
