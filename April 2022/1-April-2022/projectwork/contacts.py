import csv


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):

        if self._contacts == []:
            self._not_found()

        else:
            for contact in self._contacts:
                # if contact in self._contacts:

                self._print_contact(contact)

            # else:
            #     self._not_found()

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, name):
        for contact in self._contacts:

            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                for idx, contact in enumerate(self._contacts):
                    if contact.name.lower() == name.lower():
                        del self._contacts[idx]
                print(' ')
                print('UPDATE DATA')
                name = str(input('Contact name: '))
                phone = str(input('Contact phone : '))
                email = str(input('Email: '))
                contact = Contact(name, phone, email)
                self._contacts.append(contact)
                self._save()
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * ---')
        print(f'Name: {contact.name}')
        print(f'telephone number: {contact.phone}')
        print(f'Email: {contact.email}')
        print('--- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('***************')
        print('Not found!')
        print('***************')


def run():
    contact_book = ContactBook()
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            elif row == []:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])
    while True:
        command = str(input(" What do you want to do?\n"
                            "[a]add contact\n"
                            "[up]to update contact\n"
                            "[s]search for contact\n"
                            "[r]remove contact\n"
                            "[p]print contact\n"
                            "[q]quit\n"))
        if command == 'a':
            name = str(input('Contact name: '))
            phone = str(input('Contact phone : '))
            email = str(input('Email : '))
            contact_book.add(name, phone, email)
        elif command == 'up':
            name = str(input('Contact name: '))
            contact_book.update(name)
        elif command == 's':
            name = str(input('Contact name: '))
            contact_book.search(name)
        elif command == 'r':
            name = str(input('Contact name: '))
            contact_book.delete(name)
        elif command == 'p':
            contact_book.show_all()
        elif command == 'q':
            break
        else:
            print('command not found')


if __name__ == '__main__':
    run()
