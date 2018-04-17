class TerrainType:
    def __init__(self, name, height, color):
        self.name = name
        self.height = height
        self.color = color


regions = [TerrainType("Grass", .9, "green"),
            TerrainType("Mountain", 1, "grey"),
            TerrainType("Water", .4, "blue")]

#regionsTest = sorted(regions, key=lambda test: test.height)




for i in regions:
    print(i)
    print(i.height)
