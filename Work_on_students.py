class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
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

    def __lt__(self, other):
        if isinstance(other, Student):
            print('Not a Student!')
            return
        return self.student._average_s() < other.student1._average_s()

def st_gr_hw(students):
    sum_hw = 0
    for student in students:
        sum_hw += sum(student['Python']) / len(student['Python'])
    st = round(sum_hw / len(students), 1)
    sum_hw1 = 0
    for student in students:
        sum_hw1 += sum(student['Git']) / len(student['Git'])
    str = round(sum_hw1 / len(students), 1)
    return f'Средняя оценка по курсу "Git" за ДЗ: {str} \nСредняя оценка по курсу "Python" за ДЗ: {st}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname, age):
        self.surname = surname
        self.name = name
        self.age = age
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
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

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            print('Not a lecturer!')
            return
        return self.lecturer._average_l  > other.lecturer1._average_l()

def lt_gr_hw(lecturers):
    sum_hw = 0
    for lecturer in lecturers:
        sum_hw += sum(lecturer['Python']) / len(lecturer['Python'])
    st = round(sum_hw / len(lecturers), 1)
    sum_hw1 = 0
    for lecturer in lecturers:
        sum_hw1 += sum(lecturer['Git']) / len(lecturer['Git'])
    str = round(sum_hw1 / len(lecturers), 1)
    return f'Средняя оценка по курсу "Git" за лекции: {str} \nСредняя оценка по курсу "Python" за лекции: {st}'

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
cool_mentor.courses_attached += ['Python']


student2 = Student('Alex', 'Jackson', 'your_gender')
student2.courses_in_progress += ['Python', 'Git']
student2.courses_attached += ['Git', 'Python']
student2.finished_courses += ['Введение в программирование']
student1 = Student('Bobby', 'Ozzy', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.courses_attached += ['Git', 'Python']
student1.finished_courses += ['Введение в программирование']
student = Student('Rio', 'Eman', 'your_gender')
student.courses_in_progress += ['Python', 'Git']
student.courses_attached += ['Git', 'Python']
student.finished_courses += ['Введение в программирование']
some_student = student
student_grade_hw = student.grades, student1.grades, student2.grades


lecturer1 = Lecturer('Roy', 'Jones', 'age' )
lecturer1.courses_in_progress += ['Git']
lecturer1.courses_attached += ['Git', 'Python']
lecturer = Lecturer('Jone', 'Simse', 'age')
lecturer.courses_in_progress += ['Python']
lecturer.courses_attached += ['Git', 'Python']
some_lecturer = lecturer
lecturer_grade_hw = lecturer.grades, lecturer1.grades
student.rate_lectures(lecturer, 'Git', 9)
student.rate_lectures(lecturer, 'Git', 9)
student.rate_lectures(lecturer, 'Git', 5)
student.rate_lectures(lecturer1, 'Git', 10)
student.rate_lectures(lecturer1, 'Git', 9)
student.rate_lectures(lecturer1, 'Git', 10)
student.rate_lectures(lecturer, 'Python', 8)
student.rate_lectures(lecturer, 'Python', 8)
student.rate_lectures(lecturer, 'Python', 8)
student.rate_lectures(lecturer1, 'Python', 8)
student.rate_lectures(lecturer1, 'Python', 8)
student.rate_lectures(lecturer1, 'Python', 8)

n_reviewer = Reviewer('Jonas', 'Bobby')
n_reviewer.courses_attached += ['Python', 'Git']
some_reviewer = n_reviewer

n_reviewer.rate_hw(student2, 'Python', 10)
n_reviewer.rate_hw(student2, 'Python', 9)
n_reviewer.rate_hw(student2, 'Python', 8)
n_reviewer.rate_hw(student2, 'Git', 8)
n_reviewer.rate_hw(student2, 'Git', 9)
n_reviewer.rate_hw(student2, 'Git', 8)

n_reviewer.rate_hw(student, 'Python', 10)
n_reviewer.rate_hw(student, 'Python', 10)
n_reviewer.rate_hw(student, 'Python', 10)
n_reviewer.rate_hw(student, 'Git', 8)
n_reviewer.rate_hw(student, 'Git', 9)
n_reviewer.rate_hw(student, 'Git', 8)
n_reviewer.rate_hw(student1, 'Python', 1)
n_reviewer.rate_hw(student1, 'Python', 1)
n_reviewer.rate_hw(student1, 'Python', 1)
n_reviewer.rate_hw(student1, 'Git', 8)
n_reviewer.rate_hw(student1, 'Git', 8)
n_reviewer.rate_hw(student1, 'Git', 8)

# Задача 1; 2; 3:
print('Рецензент:', some_reviewer,'\n')
print('Лектор:', some_lecturer, '\n')
print('Студент:', some_student, '\n')

# Задача 3.2 //Сравнение студентов и лекторов по средней оценке через операторы сравнения//
student._average_s().__lt__(student1._average_s())
print(f'{student._average_s()} > {student1._average_s()}')
print(student._average_s() > student1._average_s())
print(f'{student1._average_s()} > {student2._average_s()}')
student1._average_s().__lt__(student2._average_s())
print(student1._average_s() > student2._average_s())
print(f'{student._average_s()} > {student2._average_s()}')
student._average_s().__lt__(student2._average_s())
print(student._average_s() > student2._average_s())


lecturer._average_l().__lt__(lecturer1._average_l())
print(f'\n{lecturer._average_l()} < {lecturer1._average_l()}')
print(lecturer._average_l() < lecturer1._average_l())
# Задача 4 // Средние оценки лекторов //
print('\n', st_gr_hw(student_grade_hw))
print(lt_gr_hw(lecturer_grade_hw))

