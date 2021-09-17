import random

################# Fruit classes #################


class Fruit():
    def __init__(self) -> None:
        self.flavour, self.colour = random.choice(self.varieties)


class Apple(Fruit):
    varieties = [('sour, green'), ('sweet', 'red')]


class Pear(Fruit):
    varieties = [('mellow', 'yellow'), ('sharp', 'green')]

################# Tree classes #################


class Tree():
    def __init__(self) -> None:
        self.fruits = []


class AppleTree(Tree):
    fecundity = 8
    fruit_type = Apple


class PearTree(Tree):
    fecundity = 5
    fruit_type = Pear

################# Cider classes #################


class Cider():
    def __init__(self, fruitlist) -> None:
        self.flavour = {
            "sweet": 0,
            "sour": 0,
            "mellow": 0,
            "sharp": 0
        }
        for fruit in fruitlist:
            self.flavour[fruit.flavour] += 1
