import random
from opensimplex import OpenSimplex
from PIL import Image

width = 600
height = 400
scale = 185

octaves = 3
persistence = .2
lacunarity = 5

simplex = OpenSimplex(seed=random.randint(0,1000000))

def main():
    mapNoiseGrid = generateNoiseGrid(width,height,scale,octaves,persistence,lacunarity)
    generateImg(mapNoiseGrid)

def generateNoiseGrid(width,height,scale,octaves,persistence,lacunarity):
    noiseGrid = [[r for r in range(width)] for i in range(height)]

    maxNoiseHeight = 0
    minNoiseHeight = 0
    noiseHeight = 1

    for y in range(0, height):
        for x in range(0, width):

            noiseHeight = combined(x, y) * 2 - 1
            #print(noiseHeight.real)


            if noiseHeight.real > maxNoiseHeight:
                maxNoiseHeight = noiseHeight.real
            elif noiseHeight.real < minNoiseHeight:
                minNoiseHeight = noiseHeight.real

            noiseGrid[y][x] = (noiseHeight.real-minNoiseHeight)/(maxNoiseHeight-minNoiseHeight)


    return noiseGrid


def generateImg(noiseGrid):
    im = Image.new('L', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            value = noiseGrid[y][x]
            color = int((value + 1) * 128)
            #colorMap[y][x] = color
            im.putpixel((x, y), color)
    #im.putdata(colorMap)
    im.save('noise2d.png')
    im.show()
    return





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








if __name__ == '__main__':
    main()
