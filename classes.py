import random

################# Fruit classes #################


class Fruit():
    def __init__(self) -> None:
        self.flavour, self.colour = random.choice(self.varieties)

    def __repr__(self) -> str:
        return f"<{self.flavour}, {self.colour}, {self.__class__.__name__}>"


class Apple(Fruit):
    varieties = [('sour', 'green'), ('sweet', 'red')]


class Pear(Fruit):
    varieties = [('mellow', 'yellow'), ('sharp', 'green')]

################# Tree classes #################


class Tree():
    def __init__(self) -> None:
        self.fruits = []

    def __repr__(self) -> str:
        return f"{self.fruit_type.__name__} tree"

    def blossom(self):
        for i in range(self.fecundity):
            self.fruits.append(self.fruit_type())

    def harvest(self):
        crop = self.fruits
        self.fruits = []
        return crop


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

    def __repr__(self) -> str:
        return f"And you get a barrel of {max(self.flavour, key=lambda key: self.flavour[key])} cider from the fruit!"

################# Farm classes #################


class Farm():
    def __init__(self) -> None:
        user_input = int(input(
            "Welcome to my Cider Farm, how many apple trees would you like to plant? "))
        self.orchard = [AppleTree() for x in range(user_input)]

    def __repr__(self) -> str:
        return f"The farm currently has {len(self.orchard)} trees planted"

    def spring(self):
        for tree in self.orchard:
            tree.blossom()
        print("The trees have bore fruit!")

    def autumn_harvest(self):
        autumn_crop = []
        for tree in self.orchard:
            autumn_crop.extend(tree.harvest())
        return autumn_crop

    def brew_cider(self, fruitlist):
        self.cider = Cider(fruitlist)
