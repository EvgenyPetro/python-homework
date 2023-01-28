import view
import randomizer

main_dis = {}
main_dis_r = randomizer.get_random_students()
students = []
lessons = []


def start():
    global main_dis_r
    while True:
        operation = view.get_operation()
        if operation == 1:
            student = view.add_new_student()
            if student not in students:
                main_dis[student] = {}
                students.append(student)
                if lessons:
                    for lesson in lessons:
                        main_dis[student][lesson] = []
                print(main_dis)
        elif operation == 2:
            lesson = view.add_lesson()
            lessons.append(lesson)
            for student in main_dis:
                main_dis[student][lesson] = []
            print(main_dis)
        elif operation == 3:
            student, lesson, mark = view.add_rank_student_by_lession()
            main_dis[student][lesson].append(mark)
            print(main_dis)
        elif operation == 4:
            view.show_students(students)
        elif operation == 5:
            student = view.get_student()
            for lesson in main_dis[student]:
                print(f"{lesson} - {main_dis[student][lesson]}")
        elif operation == 6:
            main_dis_r = randomizer.get_random_students()
            print(main_dis_r)
        elif operation == 7:
            student = view.get_student()
            lesson = view.get_lesson()
            print(main_dis_r[student][lesson])
            avr = sum(main_dis_r[student][lesson]) / len(main_dis_r[student][lesson])
            print(avr)
        elif operation == 8:
            lesson = view.get_lesson()
            mark_avr = []
            for student in main_dis_r:
                for i in main_dis_r[student][lesson]:
                    mark_avr.append(i)
            avr_school = sum(mark_avr) / len(mark_avr)
            print(avr_school)
        elif operation == 9:
            gold_students = []
            for student in main_dis_r:
                mark_student = []
                for lesson in main_dis_r[student]:
                    for i in main_dis_r[student][lesson]:
                        mark_student.append(i)

                if 3 not in mark_student:
                    if 2 not in mark_student:
                        if 1 not in mark_student:
                            gold_students.append(student)
            print(f"На золотую медаль претендует: {len(gold_students)} студентов")

        elif operation == 10:
            break
