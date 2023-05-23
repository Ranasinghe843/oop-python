# non-oop

""" names = ["Vera", "Chuck", "Samantha", "Roberto", "Joe", "Dave", "Tina"]
salaries = [2000, 1800, 1800, 2100, 2000, 2200, 2300]

for c in range(len(names)):
    print(f"{names[c]}, ${salaries[c]}") """

# oop
from employee import *
from reporting import *
from shift import *

employees = [
    Manager("Vera", "Schmidt", 2000, MorningShift()),
    Attendant("Chuck", "Norris", 1800, MorningShift()),
    Attendant("Samantha", "Carrington", 1800, AfternoonShift()),
    Cook("Roberto", "Jacketti", 2100, MorningShift()),
    Mechanic("Joe", "DreiBig", 2000, MorningShift()),
    Mechanic("Dave", "River", 2200, MorningShift()),
    Mechanic("Tina", "Rama", 2300, AfternoonShift()),
    Mechanic("Chuck", "Rainey", 1800, NightShift())
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees)
]

for r in reports:
    r.print_report()
    print()