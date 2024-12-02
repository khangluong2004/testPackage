import numpy as np

class AddVect:
    def __init__(self, start: list):
        self.initial = np.array(start)

    def add(self, second: list):
        self.initial += np.array(second)
        print(self.initial)

