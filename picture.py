"""
picture.py
Author: Sean Healey
Credit: W3 Schools

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/

# Colors
red = Color(0xff0000, 1.0)
orange = Color(0xffa500, 1.0)
yellow = Color(0xffff00, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
purple = Color(0x800080, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

# Colored Lines
blackline = LineStyle(1, black)
redline = LineStyle(1, red)
orangeline = LineStyle(1, orange)
yellowline = LineStyle(1, yellow)
greenline = LineStyle(1, green)
blueline = LineStyle(1, blue)
purpleline = LineStyle(1, purple)
whiteline = LineStyle(1, white)

#Colored Rectangles
redrectangle = RectangleAsset(200, 20, redline, red)
orangerectangle = RectangleAsset(200, 20, orangeline, orange)
yellowrectangle = RectangleAsset(200, 20, yellowline, yellow)
greenrectangle = RectangleAsset(200, 20, greenline, green)
bluerectangle = RectangleAsset(200, 20, blueline, blue)
purplerectangle = RectangleAsset(200, 20, purpleline, purple)
whiterectangle = RectangleAsset(200, 20, whiteline, white)

#Rainbow
Sprite(redrectangle, (0, 0))
Sprite(orangerectangle, (0, 20))
Sprite(yellowrectangle, (0, 40))
Sprite(greenrectangle, (0, 60))
Sprite(bluerectangle, (0, 80))
Sprite(purplerectangle, (0, 100))

#Sun
sun = CircleAsset(150, yellowline, yellow)
Sprite(sun, (600, 20))

#Flag
#13 Stripes, 7 red, 6 white
bluebox = RectangleAsset(150, 140, blueline, blue)
whitestripe = RectangleAsset(400, 20, whiteline, white)
redstripe = RectangleAsset(400, 20, redline, red)
stars = CircleAsset(3, whiteline, white)

for i in range(0,12):
    if ((i % 2) == 0):
        Sprite(redstripe, (0, 20*i + 200))
    else:
        Sprite(whitestripe, (0, 20*i + 200))
        
Sprite(bluebox, (0, 200))
        
for i in range(0,15):
    for j in range(0,7):
        Sprite(stars, (2 + 10*i, 205 + 20*j))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
