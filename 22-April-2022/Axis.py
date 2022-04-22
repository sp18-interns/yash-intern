from Container import Container
from Range import Range

class Axis(Container):
    range = Range()
    def __init__(self):
        Container.__init__()

    def __str__(self):
        return f"{self.label} Axis"

    def in_range(self,point):
        if(super().label == ContainerLabel.X_Axis):
            return range.in_range(point.get_x()) and point.get_y() == 0
        elif(super().label == ContainerLabel.Y_Axis):
            return range.in_range(point.get_y()) and point.get_x() == 0

        return False