import numbers


def create_pizza(name='', size=None, isveg=False, toppings=None, base='', price=0.0):
    """

    @param name: Name of the pizza
    @param size: It's a dictionary with 2 keys
        1. Diameter
        2 Label
    @param isveg: It it's a veg or non-veg pizza
        Example :-
            If it's  veg value will be true.
            If it's  non-veg value will be false.
    @param toppings: It Con

    @param base:
    @param price:
    @return:
    """
    if toppings is None:
        toppings = []
    if size is None:
        size = {'Diameter': 0.0, 'Label': ''}
    pizza = {
        'Name': name,
        'Size': size,
        'IsVeg': isveg,
        'Toppings': toppings,
        'Base': base,
        'Price': price
    }
    return pizza


def add_toppings(pizza=None, toppings=None):
    """
    This function is to add toppings to the existing toppings of the pizza.
    @param pizza: The pizza object
    @param toppings: The list of all the other toppings
        Example :-
            ["Tomatoes","Onions"]
    @return:
        It manipulates the existing pizza object and return pizza object.
    """
    if toppings is None:
        toppings = list()
    if pizza is None:
        pizza = dict()
    pizza['Toppings'].append(toppings)
    return pizza


def add_base(pizza=None, base=''):
    """
    This function is to add base to the pizza.
    @param pizza: The pizza object
    @param base: String Base which is to be added
    @return: It manipulates the existing pizza object and return pizza object.
    """
    if pizza is None:
        pizza = dict()
    pizza['Base'] = base
    return pizza


def pack_pizza(pizza):
    """

    @param pizza: The pizza object
    @param size: Float Diameter of Size
    @return: It returns the size of the box to pack the specified size of pizza.
    """

    if not (isinstance(pizza.get('Size').get('Diameter'), numbers.Number) and pizza.get('Size').get(
            'Diameter') in range(1, 29)):
        raise Exception(f'Invalid Size: "{pizza.get("Size")}". Please enter size in valid range(1-28)')
    return (f"Selecting a box of size {pizza['Size']['Diameter'] + 1}")


def choose_size(pizza):
    """

    @param pizza: The pizza object
    @return: It returns the label of pizza size according to the size in diameter specified.
    """
    size = pizza["Size"]["Diameter"]
    print(f"Pizza Size is : {size}")
    if size == 7:
        pizza["Size"]["Label"] = "Small"
        return pizza["Size"]["Label"]

    elif size in range(9, 11):
        pizza["Size"]["Label"] = "Medium"
        return pizza["Size"]["Label"]

    elif size >= 11:
        pizza["Size"]["Label"] = "Large"
        return pizza["Size"]["Label"]

    elif size >= 13:
        pizza["Size"]["Label"] = "Extra Large"
        return pizza["Size"]["Label"]
    else:
        raise Exception("Invalid Size,Please Enter Size in valid range(1-28)")


def price_pizza(pizza=None):
    """

    @param pizza: Pizza object.
    @param size: Size Label of pizza.
    @param toppings: List of toppings added to the pizza.

    @return: Price of the pizza based on the size specified
    """

    if pizza is None:
        pizza = dict()
    size = pizza["Size"]["Label"]
    price_toppings = {'cheese burst': 50.0, 'special spices': 40.0, 'extra paneer': 60.0}
    price = 0.0

    if size == 'Small':
        price = 150.0

    elif size == 'Medium':
        price = 200.0

    elif size == 'Large':
        price = 250.0

    elif size == 'Extra Large':
        price = 300.0


    if 'cheese burst' in pizza.get('Toppings'):
        price += price_toppings['cheese burst']
        return price
    elif 'special spices' in pizza.get('Toppings'):
        price += price_toppings['special spices']
        return price
    elif 'extra paneer' in pizza.get('Toppings'):
        price += price_toppings['extra paneer']
        return price
    else:
        return price
