# from To_Do_Item import To_Do_Item
from To_Do_List import To_Do_List

t1 = To_Do_List()
t = t1.items
class Menu(object):

    def __init__(self):
        pass

    def __str__(self):
        return f"Menu: "


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
                    print(t)
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
                    print(t1)
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

# m = Menu()
# print(m)
# m.choosing_from_menu()