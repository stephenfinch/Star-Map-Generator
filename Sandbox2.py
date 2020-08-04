import pygame, sys
from pygame.locals import *
from beta_logic import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((900, 900), 0, 32)
pygame.display.set_caption('Sandbox')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAYSURF.fill(BLACK)
pygame.draw.circle(DISPLAYSURF, WHITE, (450, 450), 400, 1)


star_data = star_placer()
for star in star_data:
    pygame.draw.circle(DISPLAYSURF, star.color, (star.x, star.y), star.size, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()