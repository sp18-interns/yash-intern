# Defining the Car class
class Car:
    # Think of the __init__ function as the class Constructor.
    def __init__(self, license_plate, model, color):
        self.license_plate = license_plate
        self.model = model
        self.color = color
    # Dunder method returns the license plate, model and color
    # whenever we print an instance of the class to the console

    def __repr__(self):
        return f'{self.license_plate}, {self.model}, {self.color}'


class Garage:
    # Class Constructor with four attributes
    def __init__(self):
        self.cars_added = []
        self.spots = 20
        self.car_info = {}
        self.bill = 0
    # this function returns the number of spots availables

    def spots_available(self):
        return self.spots
    # The add_car function adds a car to the parking lot
    # It takes one input parameter
    # That input parameter are the license plate, Model and Color

    def add_car(self, car):
        # This identifiers will be assigned to every car at parking
        # lot.
        # There're 20 identifiers because that's the maximum
        # capacity
        self.identifier = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1',
                           'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1',
                           'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']
        # Here we check if we have any spots available
        if self.spots > 0:
            # if we have spots available we make a list from the
            #  input using the built-in function .split().
            # then we append that list to the self.cars_added
            # attribute that we created before
            self.cars_added.append(str(car).split(', '))
            # subtract one from self.spots because we have one less
            # spot available
            self.spots -= 1
            # Here we modify the dict attribute car_info that we
            # created before and we create the keys 'code', 'license
            # plate', 'model', 'color'.
            # and we put lists as the values of the dictionary
            self.car_info = {'code': [], 'license plate': [],
                             'Model': [], 'Color': []}
            # loop through the cars_added list to access every car
            # on the parking lot
            for index, i in enumerate(self.cars_added):

                # then we append the code to the 'code' key, we
                #  append the license plate to the 'license plate'
                # key and so on and so forth
                self.car_info['code'].append(self.identifier[index])
                self.car_info['license plate'].append(i[0])
                self.car_info['Model'].append(i[1])
                self.car_info['Color'].append(i[2])
            return "car successfully added to the parking lot"
        # if zero is greater than spots then the parking lot is full
        else:
            print(f"We have {self.spots} spots available. I am sorry")
    # this function removes the car from the parking lot
    # it takes two inputs parameters: the code that was assigned to
    #  your car and the time that you had your car parked in hours

    def remove_car(self, given_code, bill_hours):

        # here we check how many codes we have in the car_info dict,
        #  we want to see how many cars are currently parked
        past_len = len(self.car_info['code'])
        # if the code passed to the function is not stored in our
        # car_info dictionary
        if given_code not in self.car_info['code']:
            print("We could not find your car. Are you sure you parked your car here? ")
        else:
            # if the given_code is in the dictionary then we loop
            #  through every code on our dictionary till we find it
            # the matching code and its index
            for index, value in enumerate(self.car_info['code']):
                if value == given_code:

                    # using the index then we can find all the car's
                    #  information
                    print("Your car's license plate is:",
                          self.car_info['license plate'][index])
                    print("Your car's model is:",
                          self.car_info['Model'][index])
                    print("Your car's color is :",
                          self.car_info['Color'][index])
                    # here we remove all the information about the
                    # car using .pop(index)
                    # and we store the code from the removed car on
                    # the removed_car_index variable
                    removed_car_index = self.car_info['code'].pop(index)
                    self.car_info['license plate'].pop(index)
                    self.car_info['Model'].pop(index)
                    self.car_info['Color'].pop(index)
                    # once the car is removed, we add one to
                    # self.spots because we have one more
                    # spot available
                    self.spots += 1
        # since we removed a car the amount of cars prior to removal
        #  must be greater than the current amount of cars
        if len(self.car_info['code']) < past_len:
            while True:
                # we check whether the str bill_hours is numeric.
                #  Example: '10', '25'
                if bill_hours.isnumeric():

                    # if bill_hours is numeric, we create a list
                    # called 'list_of_time_and_code' that contains
                    # the amount of hours that the car was parked
                    #  and the code of the car (that code is the code
                    #  from the car that was removed)
                    list_of_time_and_code = [bill_hours,
                                             removed_car_index]
                    break
                # if bill_hours is not numeric, then we prompt the
                 # following message
                else:

                    print("Your input must be an integer. Sample input: 5 ")
                # we ask the customer to enter the amount of hours
                # until the input is numeric
                    bill_hours = input(
                        "Enter for how long you were on the parking lot in hours or 'q' to quit. Example input: 5  -->  ")
              # the customer can input 'q' or 'Q' to break out of
              #  the while loop
              #
                if bill_hours in ['q', 'Q']:
                    break
            # With the list containing the bill hours and the code from the removed car now we can bill the customer
            # if the bill_hours (first element on list) is less than 20, the customer will not be charged the extra $100 fine
            if int(list_of_time_and_code[0]) < 20:
                self.bill = int(list_of_time_and_code[0]) * 5
                return f'Your total bill is ${self.bill}'
            # if the bill_hours is greater than 20 the customer will be charged an additional $100 fine
            else:
                self.bill = int(list_of_time_and_code[0]) * 5 + 100
                return f'Your total bill is ${self.bill}'
    # displays all cars in garage

    def cars_in_garage(self):
        for i in self.car_info.items():
            print(i)


# creating instances of each class
my_garage = Garage()
print(my_garage.spots_available())
my_garage.add_car(Car('LVG34', 'Ferrari', 'Red'))
my_garage.add_car(Car('UTEV3', 'Porsche', 'Blue'))
my_garage.add_car(Car('LVG34', 'Optra', 'Red'))
my_garage.add_car(Car('ABC56', 'Toyota', 'White'))

my_garage.cars_in_garage()
print(my_garage.remove_car('D1', '60'))
print(my_garage.spots_available())
