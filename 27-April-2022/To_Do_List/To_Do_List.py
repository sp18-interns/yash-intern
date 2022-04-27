from To_Do_Item import To_do_Item


class To_Do_List(object):

    def __init__(self, items=None):
        if not items:
            self.items = To_do_Item()
        self.tdl = list()

    def __str__(self):
        return self.items.__str__()

    def add_todo_items(self):
        self.tdl.append(self.items)
        return self.tdl

