from datetime import date, timedelta


class Person:
    def __init__(self, first_name, last_name, date_of_birth):

        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age = self.Calculate_Age()

    def __str__(self):
        return self.first_name
        # return f" My name is {self.first_name} {self.last_name} and date of birth year is {self.date_of_birth} and age is {self.age}"

    def Calculate_Age(self):
        # timedelta(days=365.2425)
        age = (date.today().year - self.date_of_birth)
        return age

    def __lt__(self, other):
        return (self.age < other.age)

    def __lt__(self, other):
        return (self.age < other.age)

    def __le__(self, other):
        return (self.age <= other.age)

    def __eq__(self, other):
        return (self.age == other.age)

    def __ne__(self, other):
        return (self.age != other.age)

    def __gt__(self, other):
        return (self.age > other.age)

    def __ge__(self, other):
        return (self.age >= other.age)


class Sort_Person(Person):

    def __init__(self, person_list):
        #super().__init__(first_name, last_name, date_of_birth)
        self.person_list = person_list

    def get_person_by_first_name(self, first_name):
        for person in self.person_list:
            if person.first_name == first_name:
                return person
        return None

    def __str__(self):
        my_str = ""
        print(self.person_list)
        for person in self.person_list:
            my_str = my_str + str(person) + "\n"
        return my_str

    def Sort_By_First_Name_Ascending(self):
        list_name = []
        sorted_person = []
        for person in self.person_list:
            list_name.append(person.first_name)
        list_name.sort()
        #self.person_list = list_name

        for first_name in list_name:
            # print(self.get_person_by_first_name(first_name))
            sorted_person.append(self.get_person_by_first_name(first_name))

        self.person_list = sorted_person
        return None

    def Sort_By_Last_Name_Ascending(self):
        list_name = []
        sorted_person = []
        for person in self.person_list:
            list_name.append(person.first_name)
        list_name.sort()
        self.person_list = list_name

    def Sort_By_First_Name_Descending(self):
        list_name = []
        sorted_person = []
        for person in self.person_list:
            list_name.append(person.first_name)
        list_name.sort(reverse=True)
        self.person_list = list_name

    def Sort_By_Last_Name_Descending(self):
        list_name = []
        sorted_person = []
        for person in self.person_list:
            print(person)
            list_name.append(person.last_name)
        list_name.sort(reverse=True)
        self.person_list = list_name

    def Sort_By_Age_Ascending(self):
        list_age = []
        sorted_person = []
        # for person in self.person_list:
        # int1 = person.age
        # print("Abu ", int1)
        # age1 = Person.Calculate_Age(int1)

        # list_age.append(person.age)

        # list_age.sort()

        self.person_list.sort()

    def Sort_By_Age_Descending(self):
        list_age = []
        for person in self.person_list:
            list_age.append(person.age)
        list_age.sort(reverse=True)
        self.person_list = list_age


p1 = Person('yash', 'mishra', 2000)
p2 = Person('parag', 'gunjal', 1991)
p3 = Person('abrar', 'mahadevi', 1996)
person_list = []
person_list.append(p1)
person_list.append(p2)
person_list.append(p3)
print(type(person_list))

# sort_person = Sort_Person(person_list)
# print("before sorting")
# print(sort_person)


# # print("after sorting by first name")
# # sort_person.Sort_By_First_Name_Ascending()
# # print(sort_person)

# print("Sorting by age: ")
# sort_person.Sort_By_Age_Ascending()
# print(sort_person)


# print(sort_person.person_list)

# print("after sorting by last name")
# sort_person.Sort_By_Last_Name_Descending()
# print(sort_person)


# # sort_first_name = sorted(p, key=lambda p: p.first_name)
# # print(sort_first_name)
# # print(sorted(p,reverse=True))

print(sorted(person_list))
print(sorted(person_list, key=operator.attrgetter("first_name")))
