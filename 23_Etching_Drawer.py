import shutil, sys

# Set up the constants for line characters:
UP_DOWN_CHAR = chr(9474)         # Character 9474 is '│'
LEFT_RIGHT_CHAR = chr(9472)      # Character 9472 is '─'
DOWN_RIGHT_CHAR = chr(9484)      # Character 9484 is '┌' 
DOWN_LEFT_CHAR = chr(9488)       # Character 9488 is '┐
UP_RIGHT_CHAR = chr(9492)        # Character 9492 is '└'
UP_LEFT_CHAR = chr(9496)         # Character 9496 is '┘' 
UP_DOWN_RIGHT_CHAR = chr(9500)   # Character 9496 is '┘'
UP_DOWN_LEFT_CHAR = chr(9508)    # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516) # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR = chr(9524)   # Character 9524 is '┴'
CROSS_CHAR = chr(9532)           # Character 9532 is '┼'

# Get the size of the terminal window:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
CANVAS_WIDTH -= 1

CANVAS_HEIGHT -= 5

"""The keys for canvas will be (x, y) integer tuples for the coordinate,
and the value is a set of letters W, A, S, D that tell what kind of line
should be drawn."""
canvas = {}
cursor_x = 0
cursor_y = 0


def get_canvas_string(canvas_data, cx, cy):
    """Returns a multiline string of the line drawn in canvasData."""
    canvas_str = ''

    """canvasData is a dictionary with (x, y) tuple keys and values that
    are sets of 'W', 'A', 'S', and/or 'D' strings to show which
    directions the lines are drawn at each xy point."""
    for row_num in range(CANVAS_HEIGHT):
        for column_num in range(CANVAS_WIDTH):
            if column_num == cx and row_num == cy:
                canvas_str += '#'
                continue


            cell = canvas_data.get((column_num, row_num))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvas_str += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set('D')):
                canvas_str += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvas_str += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvas_str += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvas_str += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvas_str += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvas_str += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvas_str += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvas_str += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvas_str += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvas_str += CROSS_CHAR
            elif cell == None: 
                canvas_str += ' '
        canvas_str += '\n'
    return canvas_str
            



