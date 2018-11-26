"""
A monochrome screen is stored as a single array of bytes, allowing 8
    consecutive pixels to be stored in 1 byte. The screen has width w,
    where w is divisible by 8 So that no byte is split across rows. The
    height of the screen can be derived from the length of the array.
    Implement a function that draws a horizontal line from (x1, y) to
    (x2, y).

"""


def ones_vector(x):
    sum = 0
    for i in range(x+1):
        sum += 2**i
    return sum


def draw_line(screen, width, x1, x2, y):
    length = abs(x2-x1)

    if length < width:
        mask = ones_vector(length) >> x1 << (width - 1 -x2)
        screen[y] = bin(screen[y] | mask)

    return screen


if __name__ == "__main__":
    screen = [0]
    print(bin(0))

    print(draw_line(screen, 8, 0, 4, 0))

