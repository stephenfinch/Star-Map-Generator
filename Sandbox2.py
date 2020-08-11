import pygame, sys
from pygame import Surface
from pygame.locals import *
from beta_logic import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y), 0, 32)                      #Main Display
STARFIELDSURF = Surface((field_x + (2 * field_buffer), field_y + (2 * field_buffer)))   #Starfield
STARFIELDSURF_HOLD = Surface((field_x + (2 * field_buffer), field_y + (2 * field_buffer)))  #Holdover
OPTIONSURF = Surface((screen_x - field_x - 2 * field_buffer, screen_y))                 #Option Bar
pygame.display.set_caption('StarMap')
display_changed = False
click_active = False
click_action = ("", 0)
sliding = False

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
NIGHTSKY = (7, 11, 15)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
NEWBLUE = (43, 67, 244)

field_point = (int(screen_x - field_x - 2 * field_buffer), int((screen_y - field_y - 2 * field_buffer) / 2))
click_areas = [((0, 0), (100, 100))]



def star_generator():
    draw_initial()
    star_data = star_placer()
    for star in star_data:
        pygame.draw.circle(STARFIELDSURF, star.color, (star.x, star.y), star.size, 0)

    list_of_lines = random_line_placer(star_data, 10, [3,6])
    for line in list_of_lines:
        pygame.draw.aalines(STARFIELDSURF, WHITE, False, line, 1)
    STARFIELDSURF_HOLD.blit(STARFIELDSURF,(0, 0))

def star_show():
    STARFIELDSURF.blit(STARFIELDSURF_HOLD,(0, 0))


def draw_initial():
    DISPLAYSURF.fill(BLACK)
    STARFIELDSURF.fill(BLACK)
    pygame.draw.circle(STARFIELDSURF, NIGHTSKY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), 400, 0)
    pygame.draw.circle(STARFIELDSURF, GRAY, (int(field_x / 2 + field_buffer), int(field_y / 2 + field_buffer)), 400, 1)
    OPTIONSURF.fill(WHITE)
    for button in Button_List:
        button.draw(OPTIONSURF)

def buttons_initial():
    return [Input.Button(name="reset", text="Recalculate", color=(127, 127, 127), area=((0, 0), (200, 75)), size=(200, 75), border_size=4)]

def define_interactions():
    temp_list = []
    entry = 0
    for button in Button_List:
        temp_list.append(("Button", button.area, button.name, entry))
        entry += 1
    return temp_list

def draw_surfaces():
    DISPLAYSURF.blit(STARFIELDSURF, field_point)
    DISPLAYSURF.blit(OPTIONSURF, (0, 0))

Button_List = buttons_initial()
click_areas = define_interactions()
draw_initial()
star_generator()
draw_surfaces()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            click_active = False
            if click_action[0] == "Button":
                Button_List[click_action[1]].active = False
                click_action = ("", 0)
            if not display_changed:
                draw_initial()
                display_changed = True
            star_show()
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for entry in click_areas:
                if entry[1][0][0] <= mouse[0] <=entry[1][1][0] and entry[1][0][1] <= mouse[1] <=entry[1][1][1]:
                    if entry[0] == "Button":
                        Button_List[entry[3]].active = True
                        click_active = True
                        click_action = ("Button", entry[3])
                    if not display_changed:
                        draw_initial()
                        display_changed = True
                    star_generator()
        if sliding and event.type == MOUSEMOTION:
            a=1
    if display_changed:
        display_changed = False
        draw_surfaces()
    pygame.display.update()