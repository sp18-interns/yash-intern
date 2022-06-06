import datetime

from experience import  Experience
from Person import Person

if __name__ == "__main__":
    print("This is to check the system is setup fine")


    start_date = datetime.datetime(2019, 4, 1)
    end_date = datetime.datetime(2020, 2, 1)
    exp1 = Experience(start_date, end_date, "ICICI", "BSM", )
    print(not isinstance(exp1,Experience))

    start_date = datetime.datetime(2022, 1, 1)
    end_date = datetime.datetime(2022, 2, 2)
    exp2 = Experience(start_date, end_date, "INFY", "Executive", False)

    start_date = datetime.datetime(2022, 3, 2)
    end_date = datetime.datetime(2022, 3, 2)
    exp3 = Experience(start_date, end_date, "Spark Eighteen", "Intern", True)

    parag = Person("Parag")
    #parag.add_experience("Parag")
    parag.add_experience(exp1)
    parag.add_experience(exp2)
    parag.add_experience(exp3)
    #parag.add_experience("Abrar")

   #print(parag.get_total_experience_in_years())
    #print(parag.get_total_experience_in_months())
    print(f"Parag experience in days is {parag.get_total_experience_in_days()}")
    print(f"Parag experience in months is {parag.get_total_experience_in_months()}")
    print(f"Parag experience in years is {parag.get_total_experience_in_years()}")
    # exp4 = experience.Experience()
    print(exp1)
    print(exp2)
    print(exp3)
    # print(exp4)
    print(f"Most worked company name is {parag.which_company_he_worked_most()[1]} and {parag.which_company_he_worked_most()[0]} days ")
    print(f"Least worked company name is {parag.which_company_he_worked_least()[1]} and {parag.which_company_he_worked_least()[0]} days ")

    lst = [1,5,3,2,4,2]

    par = lst.index(1)
    print(par)

    print("*" * 100)

    # for i in lst(range(0,7)):
    #     print (i)

    for i in lst:
        print(i)

    print("*" * 100)

    for i in lst:
        # if lst[i] == 2:
        if i == 2:
            print(lst[i])

    print("*" * 100)

    for index, value in enumerate(lst):
        if value == 2:
            print(index)

    # for i in range(len(lst)):
    #     print(lst[i])

    print(parag.currently_in_which_company())

    sum = 0
    for i in range(0,50):
        sum += i
    print(sum)