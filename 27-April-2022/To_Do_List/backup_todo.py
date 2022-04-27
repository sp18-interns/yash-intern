from datetime import datetime

class To_do_Item(object):

    def __init__(self):
        self.title = ''
        self.items = [-1]
        self.created_at = datetime.now()
        self.modified_at = datetime.now()

    def _get_list_data(self, notes=None):
        if not notes:
            notes = range(1, len(self.items))
        list_data = str()
        for index in notes:
            item = f"{index}. {self.items[index]}\n"
            list_data += item

        return list_data

    def __str__(self):
        return f"""
********************************************************************************
Title: {str(self.title)}
ToDos:\n{'' if not self.items else self._get_list_data()}
Created at:{self.created_at}\t\t\tModified at:{self.modified_at}
********************************************************************************
"""
    def add_title(self,title):
        self.title += title

    def add_notes(self,item):
        self.items.append(item)
        print(f"{item} added at {self.created_at}")

    def __setitem__(self, key, edit):
        self.key = key
        self.edit = edit
        if self.key not in range(1, len(self.items)):
            print('Sorry, No existing notes here to edit')
        else:
            self.items[self.key] = self.edit
            print(f"{self.edit} added at {self.modified_at}")

    def __delitem__(self, index):
        self.index = index
        if self.index not in range(1, len(self.items)):
            print(f"Sorry, No item found")
        else:
            print(f"{self.items[self.index]} deleted")
            del self.items[self.index]
        self.menu()

    def search(self, query):
        for i, item in enumerate(self.items):
            if query in self.items[item]:
                print(f'{query} found in {self.items[item]}')
                break
        else:
            print("Sorry, your search request not found")

    def choosing_from_menu(self):

        print('Welcome to your To Do List!!!\n')


        print(
            "What would you like to do?\n1.Add New: \n2.Update Existing: \n3.Search something: \n4.Delete: \n5.Show notes\n6.Show To_Do_list: \n7.Exit: ")
        try:
            input_choice = int(input('Please choose your choice(in no.s): '))
        except:
            input_choice = int(input("Sorry,wrong choice. Enter numbers only: "))
        finally:
            while True:
                if input_choice == 1:
                    input_title = input('How would you like to name your notes: ')
                    t.add_title(input_title)
                    while True:
                        try:
                            note = input("Add note or press 'E' to exit: ")
                            if note != 'E':
                                t.add_notes(note)

                            else:
                                break
                        except EOFError:
                            break
                    print(f"TODO item is :\n{t}")
                    t1.add_todo_items()
                    print(f"TODO list is :\n{t1}")
                    self.replay()

                elif input_choice == 2:
                    edit_notes_index = int(input('Choose which index you want to edit: '))
                    edit = input('Type your updated note: ')
                    t.__setitem__(edit_notes_index, edit)
                    print(To_do_Item)
                    self.replay()

                elif input_choice == 3:
                    query = input('Search: ')
                    t.search(query)
                    self.replay()

                elif input_choice == 4:
                    del_index = int(input('Choose which index you want to delete: '))
                    t.__delitem__(del_index)
                    print(t)
                    self.replay()

                elif input_choice == 5:
                    print(t, end='')
                    self.replay()

                elif input_choice == 6:
                    print(t1,end='')
                    self.replay()

                elif input_choice == 7:
                    exit(0)

                else:
                    if not self.replay():
                        break


    def replay(self):
        while True:
            choice = input('Do you want to do something more(y/n): ')
            if choice.capitalize() == 'Y' or choice.capitalize() == 'N':
                return self.choosing_from_menu()
            else:
                if choice.capitalize() != 'Y' and choice.capitalize() != 'N':
                    input('Sorry, Wrong Choice. Try again(y/n): ')
            break
        return ''
from menu import Menu

if __name__ == "__main__":
    m= Menu()
    m.choosing_from_menu()




