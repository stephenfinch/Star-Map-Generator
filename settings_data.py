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

Star_Limit = (0, 1000000) #Unknown Limits
Background_Colors = {
    "Night Sky": (7, 11, 15),
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255)
}
Star_Colors = {
    "Blue": (154, 175, 255),
    "Blue-White": (202, 215, 255),
    "White": (248, 247, 255),
    "Yellow-White": (255, 244, 234),
    "Yellow": (255, 242, 161),
    "Orange": (255, 196, 111),
    "Red": (255, 96, 96)
}

Rotation_Limit = (-180, 180) #Unknown Limits
Curve_Limit = (-45, 45) #Unknown Limits
Text_Limit = (8, 40) #Unknown Limits
Show_Constellation_Lines = False
Starfield_Image_Size = (800, 800)
Options_Width = 200