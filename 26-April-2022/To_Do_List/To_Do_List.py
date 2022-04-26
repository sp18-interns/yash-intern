class TodoList(object):

    def __init__(self, title=None):
        self.title = title
        self.items = [-1]

    def print_list(self, notes=None):
        if notes is None:
            notes = range(len(self.items))

        for _ in range(1, len(notes)):
            item = f"{_}. {self.items[_]}"
            print(item)

    def __str__(self):
        return f"Title :{str(self.title)}\n{self.print_list()}"

    def add(self, item):

        self.items.append(item)

    def __setitem__(self, key, update):
        self.key = key
        self.update = update
        if self.key not in range(0,len(self.items)):
            print('Sorry, No existing notes here to update')
        else:
            self.items[self.key] = self.update
            print(f"{self.update} added")

    def __delitem__(self, index):
        self.index = index
        if self.index not in range(len(self.items)):
            print(f"Sorry, No item found")
        else:
            print(f"{self.items[self.index]} deleted")
            del self.items[self.index]
        self.menu()


    def search(self, query):
        for i, item in enumerate(self.items):
            if query in self.items:
                print(f'{query} found')
                break
        else:
            print("Sorry, your search request not found")

    def menu(self):
        print(
            "What would you like to do?\n1.Add New: \n2.Update Existing: \n3.Search something: \n4.Delete: \n5.Exit: ")
        input_choice = int(input('Please choose your choice(in no.s): '))
        while True:
            if input_choice == 1:
                add_notes = input('Add: ')
                self.add(add_notes)
                self.print_list()
                self.replay()

            elif input_choice == 2:
                update_notes_index = int(input('Choose which index you want to update: '))
                update = input('Type your updated note: ')
                self.__setitem__(update_notes_index, update)
                self.print_list()
                self.replay()

            elif input_choice == 3:
                query = input('Search: ')
                self.search(query)
                self.replay()

            elif input_choice == 4:
                del_index = int(input('Choose which index you want to delete: '))
                self.__delitem__(del_index)
                self.print_list()
                self.replay()

            elif input_choice == 5:
                exit(0)

            else:
                if not self.replay():
                    break

    def replay(self):
        while True:

            choice = input('Do you want to do something more(y/n): ')
            if choice.capitalize() == 'Y' or choice.capitalize() == 'N':
                return self.menu()



            else:
                if (choice.capitalize() != 'Y' and choice.capitalize() != 'N'):
                    input('Sorry, Wrong Choice. Try again(y/n): ')
            break


if __name__ == "__main__":
    print('Welcome to your To Do List!!!\n')
    input_title = input('How would you like to name your notes: ')
    x = TodoList(input_title)
    print(x)
    x.menu()
