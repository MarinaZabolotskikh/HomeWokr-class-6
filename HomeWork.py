class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        compare_st = self.ave_hw() < other.ave_hw()
        if compare_st:
            print(f"{self.name} {self.surname} учится хуже, чем {other.name} {other.surname}")
        else:
            print(f"{self.name} {self.surname} учится лучше, чем {other.name} {other.surname}")
        return compare_st

    def __str__(self):
        res = f"Имя:{self.name}\n" \
              f"Фамилия:{self.surname}\n" \
              f"Средняя оценка за домашнее задание:{self.ave_hw()}\n" \
              f"Курсы в процессе изучения:{' '.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы:{' '.join(self.finished_courses)}"
        return res

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 0 < grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def ave_hw(self):
        sum_hw = 0
        count = 0
        for course in self.grades.values():
            sum_hw += sum(course)
            count += len(course)
        return round(sum_hw / count, 1)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __lt__(self, other):
        compare_lect = self.ave_rat() < other.ave_rat()
        if compare_lect:
            print(f"{self.name} {self.surname} преподает хуже, чем {other.name} {other.surname}")
        else:
            print(f"{self.name} {self.surname} преподает лучше, чем {other.name} {other.surname}")
        return compare_lect

    def __str__(self):
        res = f"Имя:{self.name}\n" \
              f"Фамилия:{self.surname}\n" \
              f"Средняя оценка за лекцию:{self.ave_rat()}"
        return res

    def ave_rat(self):
        sum_rat = 0
        count = 0
        for course in self.grades.values():
            sum_rat += sum(course)
            count += len(course)
        return round(sum_rat / count, 1)

class Reviewer(Mentor):
    def __str__(self):
        res = f"Имя:{self.name}\nФамилия:{self.surname}"
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def ave_rat_all_st(student_list, course):
    all_sum = 0
    for student in student_list:
        for cour, grades in student.grades.items():
            if cour == course:
                all_sum += sum(grades) / len(grades)
    return all_sum

def ave_rat_all_lect(lect_list, course):
    general_sum = 0
    for student in lect_list:
        for cour, grades in lect_list.grades.items():
            if cour == course:
                general_sum += sum(grades) / len(grades)
    return general_sum

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ["Git"]

student_2 = Student("Tom", "Jerry", "m")
student_2.courses_in_progress += ["Python"]
student_2.finished_courses += ["Git"]

reviewer_1 = Reviewer("Ivan", "Petrov")
reviewer_1.courses_attached += ["Python"]
reviewer_1.courses_attached += ["Git"]

reviewer_2 = Reviewer("Chip", "Dale")
reviewer_2.courses_attached += ["Python"]
reviewer_2.rate_hw(student_2, "Git", 7)

lecturer_1 = Lecturer("John", "Smit")
lecturer_1.courses_attached += ["Python"]
lecturer_2 = Lecturer("Robin", "Good")
lecturer_2.courses_attached += ["Git"]

student_1.rate_lec(lecturer_1, "Python", 8)
student_1.rate_lec(lecturer_2, "Git", 4)
student_2.rate_lec(lecturer_1, "Python", 10)
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_1.rate_hw(student_1, "Git", 6)
reviewer_2.rate_hw(student_2, "Git", 7)
reviewer_2.rate_hw(student_2, "Git", 3)
reviewer_1.rate_hw(student_2, "Python", 6)
reviewer_2.rate_hw(student_1, "Python", 10)

print(reviewer_2)
print(lecturer_1)
print(student_2)
print(student_2.grades)
print(student_1.grades)
print(student_2 < student_1)
print(lecturer_1 < lecturer_2)

