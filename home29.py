class GroupFullError(Exception):
    pass


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o., record book: {self.record_book}"

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.record_book))

    def __eq__(self, other):
        return (self.first_name, self.last_name, self.record_book) == (other.first_name, other.last_name, other.record_book)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullError("Неможливо додати більше 10 студентів")
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(s) for s in self.group)
        return f'Number:{self.number}\n{all_students}'


# Тестування
gr = Group('PD2')

for i in range(10):
    st = Student('Male', 20+i, f'Name{i}', f'Surname{i}', f'RB{i}')
    gr.add_student(st)

try:
    st_extra = Student('Female', 21, 'Extra', 'Student', 'RBX')
    gr.add_student(st_extra)
except GroupFullError as e:
    print(e)
print(gr)
