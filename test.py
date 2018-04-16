"""
from opensimplex import OpenSimplex
from PIL import Image

height = int(input("Enter in the map height: "))
width = int(input("Enter in the map width: "))


def generateGrid():
    simplex = OpenSimplex()
    im = Image.new('L', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            value = simplex.noise2d(x , y )
            color = int((value + 1) * 128)
            im.putpixel((x, y), color)
    im.save('noise2d.png')
    im.show()



if __name__ == '__main__':
    main()
"""



"""
import random
import math

random.seed(0)

def generateWhiteNoise(width,height):
    noise = [[r for r in range(width)] for i in range(height)]

    for i in range(0,height):
        for j in range(0,width):
            noise[i][j] = random.randint(-50,50)

    return noise

noise = generateWhiteNoise(10,10)

for i in noise:
    print()
    for o in i:
      print(o,end='')
"""



"""
for i in noise:
    print()
    for o in i:
      print(o,end='')
"""


"""import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640,480))
"""
