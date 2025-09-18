class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display_details(self):
        print("name: "+self.name)
        print(f"age: {self.age}")


class Employee(Person):
    def __init__(self, name="", age=0, salary=0.0):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"salary: {self.salary}")


person = Person("Toto", 20)
person.display_details()
employee = Employee("Toto", 20, 2000.5)
employee.display_details()
