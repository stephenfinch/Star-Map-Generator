# (x, y) system bounded by a circle

# SETTINGS PAGE
'''
Number of stars - int (0, 1000000)
Background Color - int[index of array of options] (black, white, blue, yellow, )
Star Color - int[index of array of options] (black, white, blue, yellow, )
Rotate Text - int (-180, 180)
Curve Text - int (0, 45)
Size Text - int 
Connect Constellation Stars - bool
Image Size
'''

# ATTRIBUTES OF STARS
'''
location - tuple
Size - int
Color - RGB
'''

# ATTRIBUTES OF CONSTELLATIONS
'''
Location - int, int
Size - int
*Rotation - int
*Curvature - int
'''


import random
import math
from settings_data import *

field_buffer = 50
field_inner_buffer = 1
Options_Width = 200
field_x, field_y = 800, 800
screen_x, screen_y = field_x + Options_Width + 2 * field_buffer, field_y + 2 * field_buffer
star_list = []
number_of_stars = 5000 #was 3000
star_max_size = 3
star_colors = ['white', 'red', 'blue', 'yellow'] #star colors data comes from settings page, the shade of that color 
star_colors_RGB = [(43, 67, 244), (30, 75, 170), (50, 123, 230), (13, 33, 190), (0, 0, 255)]
ex = 30

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (x,y)
        self.size = int(math.floor(random.random() ** ex * star_max_size))
        if self.size == 1:
            self.size = 0
        #find better way of getting color data from settings
        self.color = (43, 67, 244)
        #self.amp = random.randint(self.size+1, star_max_size)/star_max_size
        #self.color = [self.color[0]*self.amp, self.color[1]*self.amp, self.color[2]*self.amp]


def star_placer():
    stars_added = 0
    star_list = []
    while stars_added < number_of_stars:
        x, y = random.randint(0, screen_x), random.randint(0, screen_y)
        if is_in_circle(x,y):
            star_list.append(Star(x,y))
            stars_added += 1
    return star_list


def random_line_placer(stars, groups, lines):
    lines = random.randint(lines[0], lines[1])
    output_stars = []
    for _ in range(groups):
        temp_seed = stars[random.randint(0,len(stars)-1)] #pick a random starting star
        temp_seed.size = 3 #this is not working yet. need to fine a way to resize the star once it has been picked
        temp_star_list = []
        for star in stars:
            if abs(star.x-temp_seed.x) + abs(star.y-temp_seed.y) <= 100:
                temp_star_list.append(star.location)
                star.size = 3 #this is not working yet. need to fine a way to resize the star once it has been picked
        for x in range(lines):
            temp_star_list.append(temp_star_list[random.randint(0,len(temp_star_list)-1)])
        temp_star_list = temp_star_list[-lines:]
        output_stars.append((temp_star_list))
    return output_stars


r = field_x / 2 - field_inner_buffer #raduis
Xcenter = Ycenter = field_x / 2 + field_buffer

def is_in_circle(x, y):
    test = (x - Xcenter) ** 2 + (y - Ycenter) ** 2 <= r ** 2
    return test


    
