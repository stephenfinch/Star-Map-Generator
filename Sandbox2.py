import pygame, sys
from pygame import Surface
from pygame.locals import *
from beta_logic import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y), 0, 32)                      #Main Display
STARFIELDSURF = Surface((field_x + (2 * field_buffer), field_y + (2 * field_buffer)))   #Starfield
OPTIONSURF = Surface((screen_x - field_x - 2 * field_buffer, screen_y))                 #Option Bar
pygame.display.set_caption('StarMap')

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
NIGHTSKY = (7, 11, 15)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NEWBLUE = (43, 67, 244)

DISPLAYSURF.fill(BLACK)
pygame.draw.circle(DISPLAYSURF, GRAY, (450, 450), 400, 1)
STARFIELDSURF.fill(BLACK)
#pygame.draw.circle(STARFIELDSURF, NIGHTSKY, (field_x / 2 + field_buffer, field_y / 2 + field_buffer), 400, 0)
#pygame.draw.circle(STARFIELDSURF, GRAY, (field_x / 2 + field_buffer, field_y / 2 + field_buffer), 400, 1)


star_data = star_placer()
for star in star_data:
    pygame.draw.circle(STARFIELDSURF, star.color, (star.x, star.y), star.size, 0)

OPTIONSURF.fill(WHITE)

field_point = (screen_x - field_x - 2 * field_buffer, (screen_y - field_y - 2 * field_buffer) / 2)
DISPLAYSURF.blit(STARFIELDSURF, field_point)
DISPLAYSURF.blit(OPTIONSURF, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()