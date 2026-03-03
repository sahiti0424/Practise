class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        return self.grade >= 50

    def describe(self):
        status = "Passing" if self.is_passing() else "Failing"
        return f"{self.name} — Grade: {self.grade} — {status}"


#instance
s1 = Student("Sahiti", 85)
s2 = Student("Priya", 40)

print(s1.describe())   
print(s2.describe())   