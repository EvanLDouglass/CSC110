# Evan Douglass
# HW: Tic-Tac-Toe
# Grade at standard

# This program draws two tic-tac-toe boards with a snapshot of a game in progress
# using the Gui3 module for graphics.

import Gui3

# Set width and height of canvas
canvas_width = 690
canvas_height = 360

# Main
def main():
    # Create a window
    win = Gui3.Gui()
    # Title: Tic-Tac-Toe
    win.title('Tic-Tac-Toe')
    # Create canvas
    canvas = win.ca(canvas_width, canvas_height)
    # Draw 2 boards
    drawBoard(-315, -150, canvas)
    drawBoard(15, -150, canvas)
    # Draw an X in the center, bottom right corner, middle left of each board
    # First board
    drawX(-215, -50, canvas)
    drawX(-115, -150, canvas)
    drawX(-315, -50, canvas)
    #Second board
    drawX(115, -50, canvas)
    drawX(215, -150, canvas)
    drawX(15, -50, canvas)
    # Draw an O in the bottom left corner and upper left corner of each board
    # First board
    drawO(-315, -150, canvas)
    drawO(-315, 50, canvas)
    # Second board
    drawO(15, -150, canvas)
    drawO(15, 50, canvas)
    # Call mainloop
    win.mainloop()

# Draw board function
# Parameters: bottom left corner of bounding box, canvas
# Draws the tic-tac-toe board in the canvas
def drawBoard(x, y, canvas):
    canvas.line([[x, y+100], [x+150, y+100], [x+300, y+100]], width=3)
    canvas.line([[x, y+200], [x+150, y+200], [x+300, y+200]], width=3)
    canvas.line([[x+100, y], [x+100, y+150], [x+100, y+300]], width=3)
    canvas.line([[x+200, y], [x+200, y+150], [x+200, y+300]], width=3)

# Draw X function
# Parameters: bottom left corner of bounding box, canvas
# Draws an X figure
def drawX(x, y, canvas):
    canvas.line([[x+10, y+10], [x+50, y+50], [x+90, y+90]], width=7)
    canvas.line([[x+10, y+90], [x+50, y+50], [x+90, y+10]], width=7)

# Draw O function
# Parameters: bottom left corner of bounding box, canvas
# Draws an O figure
def drawO(x, y, canvas):
    canvas.circle([x+50, y+50], 40, width=7)

# Call main
main()
