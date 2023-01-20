def write_contact_in_phonebook(contact):
    with open("phonebook.txt", "a") as file:
        file.write(f"{contact}\n")
