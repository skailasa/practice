"""
Implement a 'paint-fill' function that one might see on many image
    editing programs. That is, given a screen represented by a 2D array
    of colours, a point and a new colour fill in the surrounding area
    until the colour changes from the original colour.
"""


SCREEN = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 10, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 10, 1],
]


VISITED = []  # keep track of pixels which have been coloured


def paint_fill(screen, x, y, colour=0):

    if (x, y) in VISITED:
        return

    screen[x][y] = colour
    VISITED.append((x, y))

    if x+1 < len(screen):
        paint_fill(screen, x+1, y, colour)

    elif y+1 < len(screen[0]):
        paint_fill(screen, x, y+1, colour)

    elif x-1 > 0:
        paint_fill(screen, x-1, y, colour)

    elif y-1 > 0:
        paint_fill(screen, x, y-1, colour)


def paint_screen(screen):
    for y in range(len(screen)):
        for x in range(len(screen[0])):
            paint_fill(screen, x, y, colour=10)

    print(screen)


if __name__ == "__main__":

    print(SCREEN)
    paint_screen(SCREEN)

