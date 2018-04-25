import random
import math
from opensimplex import OpenSimplex
from PIL import Image

"""
def generate_voronoi_diagram(width, height, num_cells):
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for i in range(num_cells):
        nx.append(random.randrange(imgx))
        ny.append(random.randrange(imgy))
        nr.append(random.randrange(256))
        ng.append(random.randrange(256))
        nb.append(random.randrange(256))
    for y in range(imgy):
        for x in range(imgx):
            dmin = math.hypot(imgx-1, imgy-1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(nx[i]-x, ny[i]-y)
                if d < dmin:
                    dmin = d
                    j = i
            putpixel((x, y), (nr[j], ng[j], nb[j]))
    image.save("VoronoiDiagram.png", "PNG")
    image.show()

generate_voronoi_diagram(500, 500, 250)
"""



def generate_voronoi_diagram(width, height, num_cells):
    noiseGrid = [[r for r in range(width)] for i in range(height)]
    vCoordinates = [[r for r in range(2)] for i in range(num_cells)]
    for i in range(num_cells):
        vCoordinates[i][0] = random.randrange(width)
        vCoordinates[i][1] = random.randrange(height)
    for y in range(0, height):
        for x in range(0, width):
            dmin = math.hypot(height-1, width-1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(vCoordinates[i][0]-x, vCoordinates[i][1]-y)
                if d < dmin:
                    dmin = d
                    j = i
            noiseGrid[y][x] = j
    return noiseGrid

print(generate_voronoi_diagram(10, 10, 3))
