import random
import math
from opensimplex import OpenSimplex
from PIL import Image

width = 500
height = 250
scale = 1
vCells = 500

octaves = 3
persistence = .2
lacunarity = 5

simplex = OpenSimplex(seed=random.randint(0,1000000))

def main():
    mapNoiseGrid = generateNoiseGrid(width,height,scale,vCells,octaves,persistence,lacunarity)

    generateImg(mapNoiseGrid)

def generateNoiseGrid(width,height,scale,vCells,octaves,persistence,lacunarity):
    noiseGrid = [[r for r in range(width)] for i in range(height)]
    vCoordinates = [[r for r in range(3)] for i in range(vCells)]

    maxNoiseHeight = 0
    minNoiseHeight = 0

    for i in range(vCells):
        vCoordinates[i][0] = random.randrange(width)
        vCoordinates[i][1] = random.randrange(height)

    for i in range(vCells):
        amplitude = 1
        frequency = 1
        noiseHeight = 0

        for o in range (0, octaves):
            samplex = vCoordinates[i][0]/scale * frequency
            sampley = vCoordinates[i][1]/scale * frequency

            simplexValue = simplex.noise2d(samplex,sampley) * 2 - 1
            noiseHeight += simplexValue * amplitude

            amplitude *= persistence
            frequency *= lacunarity


        if noiseHeight > maxNoiseHeight:
            maxNoiseHeight = noiseHeight
        elif noiseHeight < minNoiseHeight:
            minNoiseHeight = noiseHeight

        vCoordinates[i][2] = noiseHeight

    for i in range(vCells):
        vCoordinates[i][2] = (vCoordinates[i][2]-minNoiseHeight)/(maxNoiseHeight-minNoiseHeight)

    for y in range(0, height):
        for x in range(0, width):
            dmin = math.hypot(height-1, width-1)
            for i in range(vCells):
                d = math.hypot(vCoordinates[i][0]-x, vCoordinates[i][1]-y)
                if d < dmin:
                    dmin = d
                    j = i
            noiseGrid[y][x] = vCoordinates[j][2]

    return noiseGrid

class TerrainType:
    def __init__(self, name, height, color):
        self.name = name
        self.height = height
        self.color = color

regions = [TerrainType("Water Deep", .3, (0, 100, 200)),
            TerrainType("Water Shallow", .45, (0, 128, 255)),
            TerrainType("Sand", .5, (255, 230, 95)),
            TerrainType("Grass", .7, (50, 190, 0)),
            TerrainType("Grass 2", .75, (35, 145, 0)),
            TerrainType("Mountain1", .85, (140, 140, 140)),
            TerrainType("Mountain2", .95, (100, 100, 100)),
            TerrainType("Snow", 1, (255, 255, 255))]


def generateImg(noiseGrid):
    colorMap = []

    #color
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
    #Black and White
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
