from Container import Container
from Range import Range
from ContainerLabel import ContainerLabel


class Axis(Container):


    def __init__(self,point,label):
        Container.__init__(self,point,label)

    def __str__(self):
        return f"{self.label} Axis"

    def in_range(self, point):
        if super().label == ContainerLabel.X_AXIS:
            return Range.in_range(point.get_x()) and point.get_y() == 0
        elif super().label == ContainerLabel.Y_AXIS:
            return Range.in_range(point.get_y()) and point.get_x() == 0

        return False
