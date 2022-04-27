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



