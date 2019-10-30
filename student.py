class Student:
    def __init__(self, name, age, gender, house):
        self.name = name
        self.age = age
        self.gender = gender
        self.house = house

    def last_name(self):
        return self.name.split(" ")[-1]

    

harry = Student("Harry Potter", 17, "M", "Gryffindor")

print(harry.last_name())
