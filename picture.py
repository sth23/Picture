"""
picture.py
Author: Sean Healey
Credit: None (so far)

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

red = Color(0xff0000, 1.0)
orange = Color(0xffa500, 1.0)
yellow = Color(0xffff00, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
purple = Color(0x800080, 1.0)
black = Color(0x000000, 1.0)

blackline = LineStyle(1, black)
redline = LineStyle(1, red)
orangeline = LineStyle(1, orange)
yellowline = LineStyle(1, yellow)
greenline = LineStyle(1, green)
blueline = LineStyle(1, blue)
purpleline = LineStyle(1, purple)

redrectangle = RectangleAsset(200, 20, redline, red)
orangerectangle = RectangleAsset(200, 20, orangeline, orange)
yellowrectangle = RectangleAsset(200, 20, yellowline, yellow)
greenrectangle = RectangleAsset(200, 20, greenline, green)
bluerectangle = RectangleAsset(200, 20, blueline, blue)
purplerectangle = RectangleAsset(200, 20, purpleline, purple)

Sprite(redrectangle, (0, 0))
Sprite(orangerectangle, (0, 20))
Sprite(yellowrectangle, (0, 40))
Sprite(greenrectangle, (0, 60))
Sprite(bluerectangle, (0, 80))
Sprite(purplerectangle, (0, 100))

myapp = App()
myapp.run()

# add your code here /\  /\  /\


myapp = App()
myapp.run()
