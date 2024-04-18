
class Student:
    def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}
      self.courses_attached = []

    def rate_lecturer(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress
                and grade in range(0, 11)):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        total_grades = 0
        all_grades = 0

        for grade in self.grades.values():
          total_grades += sum(grade)
          all_grades += len(grade)

        if total_grades:
            return total_grades / all_grades
        else:
            return 0

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grade()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)} \n"

    def __lt__(self, other):

        if self.avg_grade() < other.avg_grade():
            return f"Студент {self.name} {self.surname} выполнил домашние задания хуже чем студент {other.name} {other.surname}! \n"
        else:
            return f"Студент {other.name} {other.surname} выполнил домашние задания хуже чем студент {self.name} {self.surname}! \n"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}




class Lecturer(Mentor):

    def avg_grade(self):
        total_grades = 0
        all_grades = 0

        for grade in self.grades.values():
              total_grades += sum(grade)
              all_grades += len(grade)

        if total_grades:
              return total_grades / all_grades
        else:
              return 0

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()} \n"

    def __lt__(self, other):

        if self.avg_grade() < other.avg_grade():
            return f"Студенты считают, что {self.name} {self.surname} преподносит информацию хуже, чем {other.name} {other.surname}! \n"
        else:
            return f"Студенты считают, что {other.name} {other.surname} преподносит информацию хуже, чем {self.name} {self.surname}! \n"



class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_student = Student('Ruoy', 'Eman', 'woman')
some_student2 = Student('Iva','Lavr','male')

some_student.finished_courses += ['Введение в программирование']
some_student2.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer2 = Reviewer('Squid', 'Squidward')
some_reviewer.courses_attached += ['Python', 'Git']
some_reviewer2.courses_attached += ['Python', 'Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer2 = Lecturer('Lol', 'Kekovich')
some_lecturer.courses_attached += ['Python', 'Git']
some_lecturer2.courses_attached += ['Python', 'Git']

some_student.courses_in_progress += ['Python', 'Git']
some_student2.courses_in_progress += ['Python', 'Git']

some_student.rate_lecturer(some_lecturer, 'Python',10)
some_student.rate_lecturer(some_lecturer, 'Python',9)
some_student.rate_lecturer(some_lecturer, 'Git',10)
some_student.rate_lecturer(some_lecturer, 'Git',10)
some_student.rate_lecturer(some_lecturer, 'Git',10)
some_student2.rate_lecturer(some_lecturer, 'Python',10)
some_student2.rate_lecturer(some_lecturer, 'Python',10)
some_student2.rate_lecturer(some_lecturer, 'Git',10)
some_student2.rate_lecturer(some_lecturer, 'Git',10)
some_student2.rate_lecturer(some_lecturer, 'Git',10)

some_student.rate_lecturer(some_lecturer2, 'Python',9)
some_student.rate_lecturer(some_lecturer2, 'Python',9)
some_student.rate_lecturer(some_lecturer2, 'Git',8)
some_student.rate_lecturer(some_lecturer2, 'Git',10)
some_student.rate_lecturer(some_lecturer2, 'Git',7)
some_student2.rate_lecturer(some_lecturer2, 'Python',6)
some_student2.rate_lecturer(some_lecturer2, 'Python',8)
some_student2.rate_lecturer(some_lecturer2, 'Git',9)
some_student2.rate_lecturer(some_lecturer2, 'Git',9)
some_student2.rate_lecturer(some_lecturer2, 'Git',10)

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer2.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer2.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer2.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer2.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)

some_reviewer.rate_hw(some_student2, 'Python', 2)
some_reviewer2.rate_hw(some_student2, 'Python', 5)
some_reviewer.rate_hw(some_student2, 'Python', 9)
some_reviewer2.rate_hw(some_student2, 'Python', 7)
some_reviewer.rate_hw(some_student2, 'Python', 3)
some_reviewer2.rate_hw(some_student2, 'Git', 4)
some_reviewer.rate_hw(some_student2, 'Git', 5)
some_reviewer2.rate_hw(some_student2, 'Git', 8)
some_reviewer.rate_hw(some_student2, 'Git', 9)
some_reviewer2.rate_hw(some_student2, 'Git', 10)

student_list = [some_student, some_student2]
lecturers_list = [some_lecturer, some_lecturer2]

def avg_grade_course(list, course):

    for person in list:
        if course in person.grades.keys():
            avg_person_grade = 0

            for grades in person.grades[course]:
                avg_person_grade += grades
            avg_person = avg_person_grade / len(person.grades[course])

        else:
            return "Нет такого курса"

    return f"Средний бал за курс {course}: {round(avg_person, 1)} \n"

print(some_student)
print(some_student2)
print(some_reviewer)
print(some_reviewer2)
print(some_lecturer)
print(some_lecturer2)
print(some_student.__lt__(some_student2))
print(some_lecturer.__lt__(some_lecturer2))

print(avg_grade_course(student_list, "Python"))
print(avg_grade_course(student_list,"Git"))
print(avg_grade_course(lecturers_list, "Python"))
print(avg_grade_course(lecturers_list, "Git"))

