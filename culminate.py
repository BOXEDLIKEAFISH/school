import pygame

pygame.init()

background = pygame.image.load("background.png")

level1 = [
"XXXXXXXXXXXXXXXXXXXX",
]


display = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Escape of the Flopper")

wall = pygame.Surface((50, 50))
wall.fill((0, 0, 0))

floor = pygame.Surface((50, 50))
floor.fill((255, 255, 255))

def draw_level(level):
    display.blit(background, (0, 0))

    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 0:
                display.blit(floor, (x * 50, y * 50))
            elif level[y][x] == 1:
                display.blit(wall, (x * 50, y * 50))

draw_level(level1)

pygame.display.update()
input()