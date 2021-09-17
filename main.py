from classes import Apple, Pear, AppleTree, PearTree, Cider

trees = [AppleTree() for x in range(5)]

for tree in trees:
    tree.blossom()
    print(tree.fruits)

crop = []
for tree in trees:
    crop.extend(tree.harvest())

print(Cider(crop))
