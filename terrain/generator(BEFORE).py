import random
from opensimplex import OpenSimplex
from PIL import Image

width = 250
height = 250
scale =25

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

    for y in range(0, height):
        for x in range(0, width):

            amplitude = 1
            frequency = 1
            noiseHeight = 0

            for o in range (0, octaves):
                samplex = x/scale * frequency
                sampley = y/scale * frequency

                simplexValue = combined(samplex,sampley) * 2 - 1
                noiseHeight += simplexValue * amplitude

                amplitude *= persistence
                frequency *= lacunarity


            if noiseHeight.real > maxNoiseHeight:
                maxNoiseHeight = noiseHeight.real
            elif noiseHeight.real < minNoiseHeight:
                minNoiseHeight = noiseHeight.real


            noiseGrid[y][x] = noiseHeight
            noiseGrid[y][x] = (noiseGrid[y][x]-minNoiseHeight)/(maxNoiseHeight-minNoiseHeight)


    """
    for y in range(0, height):
        for x in range(0, width):
            #noiseGrid[y][x] = combined (noiseGrid[x], noiseGrid[y])
            noiseGrid[y][x] = (noiseGrid[y][x]-minNoiseHeight)/(maxNoiseHeight-minNoiseHeight)
    """
    return noiseGrid

class TerrainType:
    def __init__(self, name, height, color):
        self.name = name
        self.height = height
        self.color = color

regions = [TerrainType("Water Deep", .3, (0, 100, 200)),
            TerrainType("Water Shallow", .4, (0, 128, 255)),
            TerrainType("Sand", .45, (255, 230, 95)),
            TerrainType("Grass", .55, (50, 220, 0)),
            TerrainType("Grass 2", .6, (35, 145, 0)),
            TerrainType("Mountain1", .7, (140, 140, 140)),
            TerrainType("Mountain2", .95, (100, 100, 100)),
            TerrainType("Snow", 1, (255, 255, 255))]


def generateImg(noiseGrid):

    
    colorMap = []

    im = Image.new('RGB', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            currentHeight = noiseGrid[y][x]
            for i in regions:
                if currentHeight.real <= i.height:
                    color = i.color
                    break
            colorMap.append(color)
            #im.putpixel((x, y), color)
    im.putdata(colorMap)
    im.save('noise2d.png')
    im.show()
    return

    """

    colorMap = []
    im = Image.new('L', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            value = noiseGrid[y][x]
            color = int((value.real + 1) * 128)
            colorMap.append(color)
            #im.putpixel((x, y), color)
    im.putdata(colorMap)
    im.save('noise2d.png')
    im.show()
    return

    """



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
