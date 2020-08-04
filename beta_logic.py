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


screen_x, screen_y = 900, 900
star_list = []
number_of_stars = 100 
star_max_size = 5
star_colors = ['white', 'red', 'blue', 'yellow'] #star colors data comes from settings page, the shade of that color 
star_colors_RGB = [(43, 67, 244), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
ex = 2

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (x,y)
        self.size = math.floor(random.random() ** ex * star_max_size) + 1
        self.amp = random.randint(self.size, star_max_size)
        #self.color = star_colors_RGB[random.randint(0, len(star_colors_RGB) - 1)]
        self.color = (43, 67, 244)

    def cluster(self):
        pass #test without first


def star_placer():
    stars_added = 0
    while stars_added < number_of_stars:
        x, y = random.randint(0, screen_x), random.randint(0, screen_y)
        #if is_in_circle(x,y):
        star_list.append(Star(x,y))
        stars_added += 1
    return star_list


r = 390 #raduis
Xmin = Ymin = 5
Xmax = Ymax = 795

def is_in_circle(x, y):
    confines = r ** 2 - (Xmin ** 2 + Xmax ** 2 + Ymin ** 2 + Ymax ** 2)
    test = x ** 2 - x*(Xmin + Xmax) - y*(Ymin + Ymax) + y ** 2 <= confines
    return test


