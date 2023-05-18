# non-oop

""" names = ["Vera", "Chuck", "Samantha", "Roberto", "Joe", "Dave", "Tina"]
salaries = [2000, 1800, 1800, 2100, 2000, 2200, 2300]

for c in range(len(names)):
    print(f"{names[c]}, ${salaries[c]}") """

# oop
from employee import *

employees = [
    Manager("Vera", 2000),
    Attendant("Chuck", 1800),
    Attendant("Samantha", 1800),
    Cook("Roberto", 2100),
    Mechanic("Joe", 2000),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300)
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")