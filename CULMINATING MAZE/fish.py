import pygame
import time

pygame.init()   # Initialize pygame
display = pygame.display.set_mode((1000, 1000))   # Set display size
pygame.display.set_caption("Escape of the Flopper")   # Set display caption


bert = pygame.image.load("bert.png")
bert = pygame.transform.scale(bert, (1000, 1000))
bert = bert.convert()

display.blit(bert, (0, 0))

font = pygame.font.SysFont('Arial', 70)
text = font.render('You won the game!!' , True, (0, 0, 0))
display.blit(text, (100, 170))

pygame.display.update()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

