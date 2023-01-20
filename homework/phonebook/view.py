def get_type():
    type = int(input("1 - записать контакт / 2 - показать контакты: "))
    return type


def get_contact():
    id = input("Введите id: ")
    first_name = input("Введите имя: ")
    second_name = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    comment = input("Введите кометарий: ")
    return (f"{id};{first_name};{second_name};{phone};{comment}")


def get_view():
    out = int(input(
        "Как вы хотите вывести данные: "
        "1-Отсортировать по id / 2-Отсортировать по имени / 3-показать только имя и фамилию "))
    return out
