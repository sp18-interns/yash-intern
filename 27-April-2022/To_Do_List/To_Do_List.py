from To_Do_Item import To_Do_Item
"""
Importing the to_do_item class as to_do_list has composition of to_do_items
"""


class To_Do_List(object):
    """
    Creating a class of to_do_list to contain all the to_do_items
    """

    def __init__(self, items=None):
        """

        @param items: Object of To_do_Item class as To_do_list has To_do_Items
        """
        if not items:
            self.items = To_Do_Item()
        self.tdl = list()

    def __str__(self):
        """

        @return: to print the to_do_list object like a list of to_do_items
        """
        return f"""
**********************************************************************
Title :{(''.join(map(str, self.items.title)))}
Todos : {self._get_list_todos()}
"""

    def add_todo_items(self):
        """

        @return: list containing the to_do_items
        """
        self.tdl.append(self.items._get_list_data())
        return self.tdl

    def _get_list_todos(self, todos=None):
        """

        @param todos: To take the length of todolist list
        @return: to return the contents(todoitems) of the todolist
        """
        if not todos:
            todos = range(len(self.tdl))
        list_data = str()
        for index in todos:
            item = f"Todo Item: {index+1}.\tNotes: {self.tdl[index]}\n"
            list_data += item
        return list_data