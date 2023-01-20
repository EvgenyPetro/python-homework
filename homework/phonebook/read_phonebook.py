def read_contact_in_phonebook():
    with open("phonebook.txt", "r") as file:
        arr = []
        for i in file.read().splitlines():
            arr.append(i)
        return arr


def get_first_name_and_second_name():
    arr = []
    for i in read_contact_in_phonebook():
        a = i.split(";")
        arr.append(f"{a[1]}-{a[2]}")
    return arr


def sorting_phonebook_by_id():
    arr = read_contact_in_phonebook()
    return list(sorted(arr, key=lambda x: x[0]))


def sorting_phonebook_by_first_name():
    arr = read_contact_in_phonebook()
    return list(sorted(arr, key=lambda x: x[2]))
