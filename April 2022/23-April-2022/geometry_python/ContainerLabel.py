# Python code to demonstrate enumerations
# Access and comparison

# importing enum for enumerations
import enum


# creating enumerations using class
class ContainerLabel(enum.Enum):
    FIRST_QUADRANT = 1
    SECOND_QUADRANT = 2
    THIRD_QUADRANT = 3
    FOURTH_QUADRANT = 4
    X_AXIS = 5
    Y_AXIS = 6


# Accessing enum member using value
print("The enum member associated with value 2 is : ", end="")
print(ContainerLabel(5))

# Accessing enum member using name
print("The enum member associated with name first_quadrant is : ", end="")
print(ContainerLabel['FIRST_QUADRANT'])

# Assigning enum member
mem = ContainerLabel.SECOND_QUADRANT

# Displaying value
print("The value associated with second_quadrant is : ", end="")
print(mem.value)

# Displaying name
print("The name associated with second_quadrant is : ", end="")
print(mem.name)

# Comparison using "is"
if ContainerLabel.FIRST_QUADRANT is ContainerLabel.SECOND_QUADRANT:
    print("FIRST_QUADRANT AND SECOND_QUADRANT ARE SAME QUADRANTS")
else:
    print("FIRST_QUADRANT AND SECOND_QUADRANT ARE DIFFERENT QUADRANTS")

# Comparison using "!="
if ContainerLabel.X_AXIS != ContainerLabel.Y_AXIS:
    print("X AXIS and Y AXIS are different")
else:
    print("X AXIS AND Y AXIS are same")
