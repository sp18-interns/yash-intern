from Container import Container
from Range import Range
from ContainerLabel import ContainerLabel

class Quadrant(Container):

    rangeX = Range()
    rangeY = Range()

    def __init__(self, label, rangeX, rangeY, points):

        super().__init__(points, label)
        super(label)
        self.rangeX = rangeX
        self.rangeY = rangeY

    def __str__(self):
        return f"{self.label}-Quadrant"



    def in_range(self, point):
        return self.rangeX.in_range(point.getX()) and self.rangeY.in_range(point.getY())

