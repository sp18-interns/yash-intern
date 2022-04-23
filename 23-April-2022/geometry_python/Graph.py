from ContainerLabel import ContainerLabel
from Point import Point
from Range import Range
from Quadrant import Quadrant
from LinkedList import LinkedList
from Container import Container
from Axis import Axis
import sys
from Operation import Operation

class Graph:
    origin = Point(0, 0, "origin")


    def __init__(self,label):

        self.label = label
        points = LinkedList()
        points.insert(Graph.origin)
        containers ={"ContainerLabel.FIRST_QUADRANT" : Quadrant(ContainerLabel.FIRST_QUADRANT, range(0, sys.maxsize),range(0, sys.maxsize)),'\n'
                    "ContainerLabel.SECOND_QUADRANT" : Quadrant(ContainerLabel.SECOND_QUADRANT,range(sys.minsize, 0),range(sys.maxsize, 0)),
                     "ContainerLabel.THIRD_QUADRANT" : Quadrant(ContainerLabel.THIRD_QUADRANT,range(sys.minsize, 0),range(sys.minsize, 0)),
                     "ContainerLabel.FOURTH_QUADRANT" : Quadrant(ContainerLabel.FOURTH_QUADRANT,range(0, sys.maxsize,range(sys.minsize, 0)),
                    "ContainerLabel.X_AXIS" : Axis(ContainerLabel.X_AXIS,range(sys.minsize, sys.maxsize)),
                    "ContainerLabel.Y_AXIS" : Axis(ContainerLabel.Y_AXIS,range(sys.minsize, sys.maxsize))}

    def add(self, x, y, label):
        if (find(self.x, self.y, self.label) == None):
            point = Point(self.x, self.y, self.label)
            points.insert(point)
            notifyAll(Operation.ADD, point)
            return point

        print(f"Adding point with x: {self.x:.2f}, y: {self.y:.2f}, label: {self.label} failed\n")
        return None


    def add(self, x, y):
        return add(x, y, f"unnamed_{getPoints().size()}")


    def getLabel(self):
        return self.label


    def setLabel(self, label):
        self.label = label


    def getPoints():
        return points


    def find(self, x, y, label):
        for point in self.points:
            if ((point.get_x() == x and point.get_y() == y) or (point.getLabel().equals(label))):
                return point

        return None


    def find(self, x, y):
        return find(x, y, "")


    def find(self, point):
        return find(point.get_x(), point.get_y(), point.get_label())


    def remove(self, point):
        found = find(point)
        if (found != None):
            self.points.remove(found)
            notifyAll(Operation.REMOVE, found)

        return found != None


    def move(self, point, newX, newY):
        if remove(point):
            return add(newX, newY, point.getLabel()) != None
        return False


    def notifyAll(self, operation, point):
        for container in containers.values():
            self.container.update(operation, point)


    def print(self):
        print("*"*100)
        for container in containers.values():
            print(f"{container.label}: points: {container.points}\n")
        print("*"*100)

