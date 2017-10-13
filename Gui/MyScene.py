# Evan Douglass
# LA: My Scene
# Grade at Plus

# This program draws a scene containing houses and trees using the Gui3 module

import Gui3

# Set height and width of the Gui window
CANVAS_HEIGHT = 300
CANVAS_WIDTH = 400

# Main function
def main():
    # Create window
    win = Gui3.Gui()
    # Create title for window
    win.title('My Scene')
    # Set size of window
    canvas = win.ca(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw background:
    # Create sky with a rectangle
    canvas.rectangle([[-CANVAS_WIDTH/2+2, -CANVAS_HEIGHT/2], [CANVAS_WIDTH/2, 
        CANVAS_HEIGHT/2-2]], fill='#00ccff')
    # Create grass with a rectangle
    canvas.rectangle([[-CANVAS_WIDTH/2+2, -CANVAS_HEIGHT/2], [CANVAS_WIDTH/2,
        0]], fill='#009900')

    # Draw 3 houses
    house(-180, -60, canvas, '#cc7722')
    house(-100, -100, canvas)
    house(70, -130, canvas, '#770077')

    # Draw 3 triangle trees
    triangleTree(100, -40, canvas, '#aaaa00')
    triangleTree(60, -60, canvas)
    triangleTree(0, -140, canvas, '#aa0000')

    # Draw 2 lollypop trees
    ovalTree(-30, -30, canvas)
    ovalTree(-CANVAS_WIDTH/2+10, -CANVAS_HEIGHT/2+5, canvas, '#ffd700')
    
    # Call mainloop method on the window object
    win.mainloop()

# Create a function to draw a house
# Parameters: bottom left corner of bounding box, color, canvas
# Outputs a house drawing
def house(x, y, canvas, color='blue'):
    # Create walls
    canvas.rectangle([[x+10, y], [x+110, y+50]], fill=color)
    # Create door
    canvas.rectangle([[x+48, y], [x+72, y+40]], fill='#996633')
    # Create roof
    upTriangle(x, y+50, 120, 30, '#993300', canvas)

# Create a function to draw a triangular tree
# Parameters: bottom left corner of bounding box, color, canvas
# Outputs a tree drawing with a triangle top
def triangleTree(x, y, canvas, color='#006600'):
    # Create treetop
    upTriangle(x, y+20, 50, 100, color, canvas)
    # Create trunk
    canvas.rectangle([[x+21, y], [x+29, y+20]], fill='brown')

# Create a function to draw a lolypop tree
# Parameters: bottom left corner of bounding box, color, canvas
# Outputs a tree drawing with an oval top
def ovalTree(x, y, canvas, color='#006600'):
    # Create treetop
    canvas.oval([[x, y+20], [x+50, y+120]], fill=color)
    # Create trunk
    canvas.rectangle([[x+21, y], [x+29, y+20]], fill='brown')
    
# Create a function to draw a triangle
# Parameters: starting point (x,y), width, height, color, canvas
# Outputs an isosceles triangle with given dimentions and color
def upTriangle(x, y, w, h, color, canvas):
    canvas.polygon(([[x, y], [x + w, y], [x + w/2, y + h]]), fill=color,
        outline='black')

# Call main
main()
