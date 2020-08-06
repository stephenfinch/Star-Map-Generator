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
Size - int
Amplitude - int
*Cluster - bool
Color (shade%) - float
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
from settings_data import Star_Colors, Star_Color_Weight

field_buffer = 50
field_inner_buffer = 1
Options_Width = 200
field_x, field_y = 800, 800
screen_x, screen_y = field_x + Options_Width + 2 * field_buffer, field_y + 2 * field_buffer
star_list = []
number_of_stars = 3000
star_max_size = 3
star_colors = ['white', 'red', 'blue', 'yellow'] #star colors data comes from settings page, the shade of that color 
star_colors_RGB = [(43, 67, 244), (30, 75, 170), (50, 123, 230), (13, 33, 190), (0, 0, 255)]
ex = 20
#star_colors_RGB = [(43, 67, 244), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
#star_colors_RGB = [(154, 175, 255), (202, 215, 255), (248, 247, 255), (255, 244, 234), (255, 242, 161), (255, 196, 111), (255, 96, 96)]
ex = 40

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (x,y)
        self.size = int(math.floor(random.random() ** ex * star_max_size))
        if self.size == 1: self.size = 0
        self.amp = random.randint(self.size, star_max_size)
        #self.color = star_colors_RGB[random.randint(0, len(star_colors_RGB) - 1)]
        #self.color = (43, 67, 244)
        total_weight = 0
        keys = []
        for entry in Star_Color_Weight:
            total_weight += Star_Color_Weight[entry]
            keys.append(entry)
        result = int(math.floor(random.random() * total_weight))
        current_weight = Star_Color_Weight[keys[0]]
        index = 0
        while result > current_weight:
            index += 1
            current_weight += Star_Color_Weight[keys[index]]
        self.color = Star_Colors[keys[index]]


    def cluster(self):
        pass #test without first


def star_placer():
    stars_added = 0
    while stars_added < number_of_stars:
        x, y = random.randint(0, screen_x), random.randint(0, screen_y)
        if is_in_circle(x,y):
            star_list.append(Star(x,y))
            stars_added += 1
    return star_list

r = field_x / 2 - field_inner_buffer #raduis
Xcenter = Ycenter = field_x / 2 + field_buffer

def is_in_circle(x, y):
    test = (x - Xcenter) ** 2 + (y - Ycenter) ** 2 <= r ** 2
    return test


