class Point:
    """

    @todo : Rephrase the docstring         
    Create a new Point object from the given float numbers,and assign a label to the point object created.
    """

    def __init__(self, x, y, label):
        """

        @param x: Value for the x-coordinate of the point object. Type - float()
        @param y: Value for the y-coordinate of the point object. Type - float()
        @param label: Value for the label of the point object. Type - str()
        """

        self.x = x
        self.y = y
        self.label = label
        assert type(x) == float and type(y) == float and type(
            label) == str, "2 float and 1 string expected respectively"

    def __str__(self):
        return f"{self.label}: ({self.x}, {self.y})"
        # return f"The point is : {self.label}({self.x},{self.y})"

    def set_x(self, x):
        """

        @param x: Value to set the new value of x-coordinate. Type - float()
        @return: None
        """

        self.x = x
        assert type(x) == float, "Float object expected."

    def get_x(self):
        """

        @return: Value of the x-coordinate of point object.
        """
        return self.x

    def set_y(self, y):
        """

        @param y: Value to set the new value of y-coordinate. Type - float()
        @return: None
        """

        self.y = y
        assert type(y) == float, "Float object expected."

    def get_y(self):
        """

        @return: Value of the y-coordinate of point object.
        """
        return self.y

    def set_label(self, label):
        """

        @param label: Value to set the new label of point object. Type - str()
        @return: None

        """

        self.label = label
        assert type(label) == str, "String object expected."

    def get_label(self):
        """

        @return: Value of the label of the point object.
        """
        return self.label

    # TODO assertion datatype
    # TODO if x & y is 0 then point will not move

    def move_coordinate_by(self, x=0.0, y=0.0):
        """

        @param x: Value to move the x-coordinate of point. Type - Float() 
        @param y: Value to move the y-coordinate of point. Type - Float()
        @return:  
        """

        self.x = self.x + x
        self.y = self.y + y
        assert type(x) == float and type(
            y) == float, "Only int or float allowed"  # TODO DONE
        print(
            f'Moving x Co-ordinate by {x} & y Co-ordinate by {y} makes the new point location as :{self}')

    def check_quadrant(self):
        """                     

        @return:
        """
        if self.x > 0 and self.y > 0:
            print(f"{self} is at first quadrant")
        if self.x < 0 and self.y > 0:
            print(f"{self} is at Second quadrant")
        if self.x < 0 and self.y < 0:
            print(f"{self} is at Third quadrant")
        if self.x > 0 and self.y < 0:
            print(f"{self} is at fourth quadrant")
        if self.x == 0 and self.y == 0:
            print(f"{self} is at origin")
        if (self.x > 0 or self.x < 0) and self.y == 0:
            print(f"{self} is at X Axis")
        if (self.y > 0 or self.y < 0) and self.x == 0:
            print(f"{self} is at Y Axis")
