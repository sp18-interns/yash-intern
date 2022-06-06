from abc import ABC, abstractmethod

class Container(ABC):

    def __init__(self,points,label):
        self.points = points
        self.label = label


    def add(self, candidate):
        self.candidate = candidate
        if self.find(self.candidate) or not(self.in_range(candidate)): return False
        print(f"Adding point {self.candidate} in {self.label}\n")
        return self.points.add(candidate)


    def find(self, candidate):
        for point in self.points:
            if ((candidate.get_x() == point.get_x() and candidate.get_y() == point.get_y()) or (point.get_label() == candidate.getLabel())):
                return True

        return False


    def remove(self, candidate):
        if (not(self.find(candidate))): return False
        print(f"Removing point {self.candidate} from {self.label}\n")
        return self.points.remove(candidate)

    @abstractmethod
    def in_range(self, point):
        pass

