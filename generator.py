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

from opensimplex import OpenSimplex
from PIL import Image

height = 10
width = 10

def main():
	noise = [[r for r in range(width)] for i in range(height)]

	simplex = OpenSimplex()
	for y in range(0, height):
		for x in range(0, width):
			noise[y][x] = simplex.noise2d(x,y)

	return noise

noise = main()

for i in noise:
    print()
    for o in i:
      print(o,end='')



"""import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640,480))
"""
