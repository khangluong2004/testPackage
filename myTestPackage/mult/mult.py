from art import *
import numpy as np

class MultVect:
    def __init__(self, start: list):
        self.initial = np.array(start)
    
    def mult(self, second: list):
        self.initial *= np.array(second)
        tprint(str(self.initial), font='random')


