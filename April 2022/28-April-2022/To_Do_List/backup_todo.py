from datetime import datetime


class To_do_Item(object):
    """
    Creating class To_do_Item consisting of title,notes and time stamps which can interact with
    each of these attributes.

    """

    def __init__(self):
        """
        class To_do_Item constructor
        Attributes : Title, Type: String
                    Items(Notes), Type: List
                    Time Stamps, Type: Date
        """
        self.title = ''
        self.items = [-1]                   # -1, used as a placeholder
        self.created_at = datetime.now()
        self.modified_at = datetime.now()

    def _get_list_data(self, notes=None):
        """

        @param notes: The length of the list containing notes
        @return: A string containing contents of the list in good form.
        """
        if not notes:
            notes = range(1, len(self.items))
        list_data = str()
        for index in notes:
            item = f"{index}. {self.items[index]}\n"
            list_data += item
        return list_data

    def __str__(self):
        """

        @return: the string when the instance of this class is passed as an argument to print function.
        """
        return f"""
********************************************************************************
Title: {str(self.title)}
ToDos:\n{'' if not self.items else self._get_list_data()}
Created at:{self.created_at}\t\t\tModified at:{self.modified_at}
********************************************************************************
"""

    def add_title(self, title):
        """

        @param title: The title of the To_Do-Item. Type = String
        @return: Title. Type = String
        """
        self.title += title
        return self.title

    def add_notes(self, item):
        """

        @param item: The item to be added to items list.
        @return: String containing To_do item details including title,content and modified date time stamp.
        """
        self.items.append(item)
        self.created_at = datetime.date()
        print(f"{item} added at {self.created_at}")
        return f"""
        ********************************************************************************
        Title: {str(self.title)}
        ToDos:\n{'' if not self.items else self._get_list_data()}
        Created at:{self.created_at}\t\t\t
        ********************************************************************************
        """

    def __setitem__(self, key, edit):
        """
        Getter Method
        @param key: The list index whose content is to be edited. Type: Integer
        @param edit: The item which will be used to replace the present item. type: String
        @return: String containing To_do item details including title,content and modified date time stamp.
        """
        self.key = key
        self.edit = edit
        if self.key not in range(1, len(self.items)):
            print('Sorry, No existing notes here to edit')
        else:
            self.items[self.key] = self.edit
            self.modified_at = datetime.today()
            print(f"{self.edit} added at {self.modified_at}")
        return f"""
        ********************************************************************************
        Title: {str(self.title)}
        ToDos:\n{'' if not self.items else self._get_list_data()}
                                                \t\t\tModified at:{self.modified_at}
        ********************************************************************************
        """

    def __delitem__(self, index):
        """

        @param index:  The index of the list,the content of which will be deleted.
        @return: None
        """
        self.index = index
        if self.index not in range(1, len(self.items)):
            print(f"Sorry, No item found")
        else:
            print(f"{self.items[self.index]} deleted")
            del self.items[self.index]

    def search(self, query):
        """

        @param query: The item which to search in notes
        @return: None
        """
        for i, item in enumerate(self.items):
            if query in self.items[item]:
                print(f'{query} found in {self.items[item]}')
                break
        else:
            print("Sorry, your search request not found")

    def choosing_from_menu(self):
        """
        The Menu method to enable user input to choose from the different methods of this class
        @return: None.
        """
        print('Welcome to your To Do List!!!\n')
        print(
            "What would you like to do?\n1.Add New: \n2.Update Existing: \n3.Search something: \n4.Delete: \n5.Show "
            "notes\n6.Exit: ")
        while True:
            try:
                input_choice = int(input('Please choose your choice(in no.s): '))
                if input_choice > 6:
                    raise Exception
            except ValueError:
                print("Sorry,wrong choice. Enter integers only: ")
            except Exception:
                print("Please enter numbers in range(1-6) only")
            else:
                while True:
                    if input_choice == 1:
                        while True:
                            try:
                                note = input("Add note or press 'E' to exit: ")
                                if note != 'E':
                                    print(self.add_notes(note))
                                else:
                                    break
                            except EOFError:
                                break
                        self.replay()

                    elif input_choice == 2:
                        edit_notes_index = int(input('Choose which index you want to edit: '))
                        edit = input('Type your updated note: ')
                        print(self.__setitem__(edit_notes_index, edit))
                        self.replay()

                    elif input_choice == 3:
                        query = input('Search: ')
                        self.search(query)
                        self.replay()

                    elif input_choice == 4:
                        del_index = int(input('Choose which index you want to delete: '))
                        self.__delitem__(del_index)
                        print(self)
                        self.replay()

                    elif input_choice == 5:
                        print(self, end='')
                        self.replay()

                    elif input_choice == 6:
                        exit(0)

                    else:
                        if not self.replay():
                            break
                break

    def replay(self):
        """
        Replay method to keep running the application till user decides to exit.
        @return: empty string
        """
        while True:
            choice = input('Do you want to do something more(y/n): ')
            if choice.capitalize() == 'Y' or choice.capitalize() == 'N':
                return self.choosing_from_menu()
            else:
                if choice.capitalize() != 'Y' and choice.capitalize() != 'N':
                    input('Sorry, Wrong Choice. Try again(y/n): ')
            break
        return ''

# TODo : doc string - Done, date in proper format- Done, handling exception- Done,
# TODO : single method to perform multiple functions, if input_choice>6 error message- Done
