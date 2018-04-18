import random
from opensimplex import OpenSimplex
from PIL import Image

width = 1000
height = 1000
scale = 185

octaves = 3
persistence = .2
lacunarity = 5

def main():
    mapNoiseGrid = generateNoiseGrid(width,height,scale,octaves,persistence,lacunarity)
    generateImg(mapNoiseGrid)

def generateNoiseGrid(width,height,scale,octaves,persistence,lacunarity):
    noiseGrid = [[r for r in range(width)] for i in range(height)]

    maxNoiseHeight = 0
    minNoiseHeight = 0

    simplex = OpenSimplex(seed=random.randint(0,1000000))
    for y in range(0, height):
        for x in range(0, width):

            amplitude = 1
            frequency = 1
            noiseHeight = 0

            for o in range (0, octaves):
                samplex = x/scale * frequency
                sampley = y/scale * frequency

                simplexValue = simplex.noise2d(samplex,sampley) * 2 - 1
                noiseHeight += simplexValue * amplitude

                amplitude *= persistence
                frequency *= lacunarity


            if noiseHeight > maxNoiseHeight:
                maxNoiseHeight = noiseHeight
            elif noiseHeight < minNoiseHeight:
                minNoiseHeight = noiseHeight


            noiseGrid[y][x] = noiseHeight

    for y in range(0, height):
        for x in range(0, width):
            noiseGrid[y][x] = (noiseGrid[y][x]-minNoiseHeight)/(maxNoiseHeight-minNoiseHeight)

    return noiseGrid

class TerrainType:
    def __init__(self, name, height, color):
        self.name = name
        self.height = height
        self.color = color

regions = [TerrainType("Water Deep", .3, (0, 100, 200)),
            TerrainType("Water Shallow", .4, (0, 128, 255)),
            TerrainType("Sand", .45, (255, 230, 95)),
            TerrainType("Grass", .65, (50, 220, 0)),
            TerrainType("Grass 2", .7, (35, 145, 0)),
            TerrainType("Mountain1", .8, (140, 140, 140)),
            TerrainType("Mountain2", .95, (100, 100, 100)),
            TerrainType("Snow", 1, (255, 255, 255))]


def generateImg(noiseGrid):
    colorMap = []

    im = Image.new('RGB', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            currentHeight = noiseGrid[y][x]
            for i in regions:
                if currentHeight <= i.height:
                    color = i.color
                    break
            colorMap.append(color)
            #im.putpixel((x, y), color)
    im.putdata(colorMap)
    im.save('noise2d.png')
    im.show()
    return


    """
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
    """

if __name__ == '__main__':
    main()
