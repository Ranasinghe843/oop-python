class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Mechanic(Employee):
    job_title = "Mechanic"

class Manager(Employee):
    job_title = "Manager"

class Cook(Employee):
    job_title = "Cook"

class Attendant(Employee):
    job_title = "Station Attendant"