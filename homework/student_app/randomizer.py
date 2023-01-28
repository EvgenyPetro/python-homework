import random

men_name = ['Эрик', 'Елисей', 'Данила', 'Вениамин', 'Роберт', 'Валентин', 'Роман', 'Артём', 'Тигран', 'Нестор', 'Мирон',
            'Андрон', 'Иосиф', 'Мир', 'Фадей', 'Даниэль', 'Ян', 'Архип', 'Прохор', 'Вячеслав', 'Кирилл', 'Клавдий',
            'Фока', 'Кир', 'Клим', 'Лукьян', 'Иван', 'Владимир', 'Даниил', 'Харитон', 'Давид', 'Парфен', 'Ираклий',
            'Остап', 'Вадим', 'Святослав', 'Наум', 'Радислав', 'Поликарп', 'Гаврила', 'Руслан', 'Даниль', 'Платон',
            'Макар', 'Назар', 'Матвей', 'Эмир', 'Юрий', 'Эрнест', 'Георгий']
men_s_name = ['Букин', 'Кутяков', 'Яматин', 'Янсон', 'Кэбин', 'Ломадуров', 'Чупалов', 'Нусинов', 'Бухарин', 'Глускин',
              'Нечаев', 'Сагадиев', 'Дёшин', 'Менде', 'Николаев', 'Пузанов', 'Сыропоршнев', 'Сияносов', 'Квасов',
              'Капралов', 'Шибалов', 'Церетели', 'Карпов', 'Полтанов', 'Свистовский', 'Дубинин', 'Половцев', 'Савинков',
              'Толстой', 'Ермолаев', 'Герасимов', 'Кунаев', 'Абумайлов', 'Лесничий', 'Андроников', 'Туманов', 'Ясько',
              'Задков', 'Буркин', 'Яранов', 'Ясавеев', 'Кондраков', 'Кобонов', 'Жванец', 'Ядренников', 'Шумилов',
              'Петраков', 'Кодица', 'Бикеев', 'Салтанов']
woman_name = ['Евгения', 'Жасмин', 'Виталина', 'Яна', 'Евдокия', 'Мелисса', 'Малика', 'Всеслава', 'Ева', 'Василиса',
              'Влада', 'Каролина', 'Инна', 'Раиса', 'Инга', 'Глафира', 'Марианна', 'Бронислава', 'Лада', 'Александра',
              'Изабелла', 'Валентина', 'Стела', 'Алина', 'Лея', 'Виктория', 'Агата', 'Эмма', 'Наталья', 'Мадина',
              'Ника', 'Оливия', 'Тамара', 'Розалия', 'Анфиса', 'Римма', 'Клара', 'Ксения', 'Медина', 'Алла', 'Юлия',
              'Марфа', 'Марьям', 'Амина', 'Ярослава', 'Юлиана', 'Надежда', 'Вероника', 'Дарья', 'Серафима']
woman_s_name = ['Гулина', 'Кидирбаева', 'Райкова', 'Игошева', 'Летавина', 'Свешникова', 'Фаммуса', 'Маланова', 'Зарица',
                'Андрианова', 'Григорьева', 'Верясова', 'Кузьмова', 'Шибалова', 'Синицына', 'Качурина', 'Савина',
                'Петракова', 'Шурьева', 'Куклачёва', 'Степанова', 'Верясова', 'Характерова', 'Антонова', 'Брюханова',
                'Кравчикова', 'Медведева', 'Долгова', 'Брязгина', 'Лапаева', 'Набокина', 'Яруллина', 'Юшкова',
                'Чюличкова', 'Моргунова', 'Казнова', 'Муратова', 'Чазова', 'Ижутина', 'Константинова', 'Казьмина',
                'Журавлёва', 'Насонова', 'Горемыкина', 'Косинова', 'Кравчука', 'Курневич', 'Уржумцева', 'Кутлыева',
                'Дорофеева']

lessons = ['алгебра', 'биология']


# 'география', 'геометрия', 'рисование',
# 'иностранный язык', 'информатика', 'история', 'литература', 'математика',
# 'обществознание', 'русский язык', 'статистика', 'технология', 'физика',
# 'физическая культура', 'химия', 'черчение', 'экология'


def get_random_students():
    students = []
    student_disc = {}

    name_number_rand = random.sample(range(50), 50)
    second_name_number_rand = random.sample(range(50), 50)

    for i in range(50):
        students.append(f"{men_name[name_number_rand[i]]} {men_s_name[second_name_number_rand[i]]}")
        students.append(f"{woman_name[name_number_rand[i]]} {woman_s_name[second_name_number_rand[i]]}")
    for student in students:
        student_disc[student] = {}
        for lesson in lessons:
            student_disc[student][lesson] = []
            for i in range(random.randint(1, 5)):
                student_disc[student][lesson].append(random.randint(1, 5))
    return student_disc