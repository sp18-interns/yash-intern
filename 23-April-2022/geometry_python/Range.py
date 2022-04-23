class Range:

    def __init__(self,start = 0.0,end = 0.0):
        self.start = start
        self.end = end

    def get_start(self):
        return self.start

    def get_end(self):
        return self.start

    def in_range(self,element):
        return self.start < element < self.end
    