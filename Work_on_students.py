class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.gender = []
        self.course_name = []
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lectures(self, lecturer, new_course, grade):
        if isinstance(lecturer, Lecturer):
            if new_course in lecturer.grades:
                lecturer.grades[new_course] += [grade]
            else:
                lecturer.grades[new_course] = [grade]
        else:
            return 'Ошибка'

    def _average_s(self):
        rec = []
        for v in self.grades.values():
            rec += v
        average_s = round(sum(rec) / len(rec), 1)
        return average_s

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_s()}' \
        f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {self.finished_courses[0]}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.surname = surname
        self.name = name
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_l(self):
        res = []
        for v in self.grades.values():
            res += v
        average = round(sum(res) / len(res), 1)
        return average

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_l()}' \
               f'\nЧитает лекции по курсу: {self.courses_in_progress[0]}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}'




cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

student1 = Student('Bobby', 'Ozzy', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.courses_attached += ['Python']
student1.finished_courses += ['Введение в программирование']
student = Student('Rio', 'Eman', 'your_gender')
student.courses_in_progress += ['Python', 'Git']
student.courses_attached += ['Python']
student.finished_courses += ['Введение в программирование']
some_student = student1
student1.__lt__(student)

lecturer1 = Lecturer('Roy', 'Jones')
lecturer1.courses_in_progress += ['Git']
lecturer = Lecturer('Jone', 'Simse')
lecturer.courses_in_progress += ['Python']
some_lecturer = lecturer1

student.rate_lectures(lecturer, 'Python', 7)
student.rate_lectures(lecturer, 'Python', 9)
student.rate_lectures(lecturer, 'Python', 8)
student.rate_lectures(lecturer1, 'Python', 5)
student.rate_lectures(lecturer1, 'Python', 7)
student.rate_lectures(lecturer1, 'Python', 9)

n_reviewer = Reviewer('Jonas', 'Bobby')
n_reviewer.courses_attached += ['Python']
some_reviewer = n_reviewer

n_reviewer.rate_hw(student, 'Python', 10)
n_reviewer.rate_hw(student, 'Python', 10)
n_reviewer.rate_hw(student, 'Python', 10)
n_reviewer.rate_hw(student1, 'Python', 6)
n_reviewer.rate_hw(student1, 'Python', 7)
n_reviewer.rate_hw(student1, 'Python', 9)


# print('Рецензент:', some_reviewer,'\n')
print('Лектор:', some_lecturer, '\n')
print('Студент:', some_student,'\n')
# lecturer.__lt__(lecturer1)
# print(average1 > average)
print(student.grades)
print(student1.grades)
