import view
import write_phonebook
import read_phonebook


def start():
    type = view.get_type()
    if type == 1:
        contact = view.get_contact()
        write_phonebook.write_contact_in_phonebook(contact)
    elif type == 2:
        out = view.get_view()
        if out == 1:
            print(read_phonebook.sorting_phonebook_by_id())
        elif out == 2:
            print(read_phonebook.sorting_phonebook_by_first_name())
        elif out == 3:
            print(read_phonebook.get_first_name_and_second_name())
        else:
            print(read_phonebook.read_contact_in_phonebook())
