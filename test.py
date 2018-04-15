from opensimplex import OpenSimplex
from PIL import Image

height = int(input("Enter in the map height: "))
width = int(input("Enter in the map width: "))

def main():
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
