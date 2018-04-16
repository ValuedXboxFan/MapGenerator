from sklearn import preprocessing
from opensimplex import OpenSimplex
from PIL import Image

width = 640
height = 480
scale = 50

octaves = 3
persistence = .5
lacunarity = 2

def main():
    mapNoiseGrid = generateNoiseGrid(width,height,scale,octaves,persistence,lacunarity)
    generateImg(mapNoiseGrid)

def generateNoiseGrid(width,height,scale,octaves,persistence,lacunarity):
    noise = [[r for r in range(width)] for i in range(height)]

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

                simplexValue = simplex.noise2d(samplex,sampley) #* 2 - 1
                noiseHeight += simplexValue * amplitude

                amplitude *= persistence
                frequency *= lacunarity


            if noiseHeight > maxNoiseHeight:
                maxNoiseHeight = noiseHeight
            elif noiseHeight < minNoiseHeight:
                minNoiseHeight = noiseHeight


            noise[y][x] = noiseHeight

    for y in range(0, height):
        for x in range(0, width):
            noise[y][x] = (noise[y][x]-minNoiseHeight)/(maxNoiseHeight-minNoiseHeight)

    return noise

def generateImg(noiseGrid):
    im = Image.new('L', (width, height))
    for y in range(0, height):
        for x in range(0, width):
            value = noiseGrid[y][x]
            color = int((value + 1) * 128)
            im.putpixel((x, y), color)
    im.save('noise2d.png')
    im.show()
    return

if __name__ == '__main__':
    main()
