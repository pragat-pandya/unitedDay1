class Person:
    def __init__(self, name ,dept):
        self.name = name
        self.dept = dept

    def get_details(self):
        return f"{self.name} - {self.dept}"

p = Person("Name", "Department")

a = p.get_details()
print(a)

p1 = Person("Name1", "Department1")

print(p1.get_details())