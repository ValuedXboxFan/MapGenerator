import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        # Add this somewhere after the event pumping and before the display.flip()
        #pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
        pygame.draw.polygon(screen,  (0, 128, 255), [[10, 10], [10, 20],[10, 30],[15, 30],[20, 20],[30,15],[30,30]], 8)


        pygame.display.flip()
