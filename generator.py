from opensimplex import OpenSimplex
from PIL import Image

width = 640
height = 480
scale = 75

octaves = 4
persistence = .25
lacunarity = 3.5

def main():
    mapNoiseGrid = generateNoiseGrid(width,height,scale,octaves,persistence,lacunarity)
    generateImg(mapNoiseGrid)

def generateNoiseGrid(width,height,scale,octaves,persistence,lacunarity):
    noiseGrid = [[r for r in range(width)] for i in range(height)]

    maxNoiseHeight = 0
    minNoiseHeight = 0

    simplex = OpenSimplex()
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

regions = [TerrainType("Water", .6, (0, 75, 255)),
            TerrainType("Grass", .8, (20, 220, 5)),
            TerrainType("Mountain1", .9, (100, 100, 100)),
            TerrainType("Mountain2", .98, (140, 140, 140)),
            TerrainType("Mountain3", 1, (255, 255, 255))]


def generateImg(noiseGrid):
    colorGrid = [[r for r in range(width)] for i in range(height)]

    im = Image.new('RGB', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            currentHeight = noiseGrid[y][x]
            for i in regions:
                if currentHeight <= i.height:
                    color = i.color
                    break
            #colorGrid[y][x] = color
            im.putpixel((x, y), color)
    #im.putdata(colorGrid)
    im.save('noise2d.png')
    im.show()
    return


    """
    im = Image.new('L', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            value = noiseGrid[y][x]
            color = int((value + 1) * 128)
            #colorGrid[y][x] = color
            im.putpixel((x, y), color)
    #im.putdata(colorGrid)
    im.save('noise2d.png')
    im.show()
    return
    """

if __name__ == '__main__':
    main()
