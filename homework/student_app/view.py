main_dis = {}
students = []
lessons = []


def get_operation():
    return int(input("""Введите действие: 
    1 - Добавление нового студента (Поля - имя, фамилия) 
    2 - Добавление предмета (добавляется всем ученикам сразу) 
    3 - Добавление оценки ученику по предмету (выбираем ученика(из существующих), выбираем предмет(из сущ.),пишем оценку) 
    4 - Показ списка учеников (имена фамилия) 
    5 - Показ листа оценок конкретного ученика 
    6 - Генерация сразу ста учеников
    7 - Вывод средней оценки ученика по одному предмету
    8 - Вывод среднего балла по школе по конкретному предмету
    9 - Вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5)
    10 - Выход из программы \n
    """))


def add_new_student():
    return input("Введите имя и фамилию: ")


def add_lesson():
    return input("Введите предмет: ")


def add_rank_student_by_lession():
    student = get_student()
    lesson = get_lesson()
    mark = int(input("Введите оценку: "))
    return student, lesson, mark


def show_students(students):
    for student in students:
        print(student)


def get_student():
    return input("Введите ученика(Имя фамилия через пробел): ")


def get_lesson():
    return input("Введите предмет: ")
