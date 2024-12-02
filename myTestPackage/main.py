from .add.add import AddVect
from .mult.mult import MultVect

def main():
    addObj = AddVect([1, 2, 3])
    addObj.add([2, 3, 5])

    multObj = MultVect([1, 2, 3])
    multObj.mult([5, 6, 7])

