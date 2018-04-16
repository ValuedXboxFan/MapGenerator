from opensimplex import OpenSimplex
from PIL import Image

width = 640
height = 480
scale = 25

def main():
    mapNoiseGrid = generateNoiseGrid(width,height,scale)
    generateImg(mapNoiseGrid)

def generateNoiseGrid(width,height,scale):
    noise = [[r for r in range(width)] for i in range(height)]

    simplex = OpenSimplex()
    for y in range(0, height):
        for x in range(0, width):
            samplex = x/scale
            sampley = y/scale
            noise[y][x] = simplex.noise2d(samplex,sampley)

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
