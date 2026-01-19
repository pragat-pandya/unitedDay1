class Person:
    def __init__(self, name ,dept):
        self.name = name
        self.dept = dept

    def get_details(self):
        return f"{self.name} - {self.dept}"

p = Person("Name", "Department")

a = p.get_details()
print(a)