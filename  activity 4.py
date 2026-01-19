# Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary


# Child class (Inheritance)
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    # override method
    def calculate_pay(self):
        return self.salary + self.bonus


# ---- Testing the program ----
employee = Employee("Rebecca", 500000)
manager = Manager("Rebecca", 500000, 100000)

print("Employee Pay:", employee.calculate_pay())
print("Manager Pay:", manager.calculate_pay())