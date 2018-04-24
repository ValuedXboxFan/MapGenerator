"""
Region class test

class TerrainType:
    def __init__(self, name, height, color):
        self.name = name
        self.height = height
        self.color = color


regions = [TerrainType("Grass", .9, "green"),
            TerrainType("Mountain", 1, "grey"),
            TerrainType("Water", .4, "blue")]

#regionsTest = sorted(regions, key=lambda test: test.height)




for i in regions:
    print(i)
    print(i.height)
"""




"""
width = 10
height = 10


#colorGrid = [width * height]

colorGrid = [[r for r in range(width)] for i in range(height)]


for y in colorGrid:
    for x in colorGrid:
        print (colorGrid[y][x])
"""

#Alternate noise generation
import random
from opensimplex import OpenSimplex

simplex = OpenSimplex(seed=random.randint(0,1000000))

def simple_curve(x, y):
    value = (simplex.noise2d(x,y))
    start = 0.4
    end = 0.6
    if value < start:
        return 0.0
    if value > end:
        return 1.0
    return (value - start) * (1/(end-start))

def plains(x, y):
    value = (simplex.noise2d(x,y))
    value = value**0.25
    value = value - 0.6
    return value

def mountains (x, y):
    value = simplex.noise2d(x*0.6, y * 3.0)
    return value * 2.0

def combined (x, y):
    m = mountains(x, y)
    p = plains(x, y)
    w = simple_curve(x, y)
    return (p * w) + (m * (1 - w))

print (combined(100, 100))
