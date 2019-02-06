"""
Stream of data about the colour of cars passing an individual point on
a road. Cars passing point have one unit interval between them. For
any pair of colours (A, B), want to know the shortest distance between
all pairs of cars of colour A and B in the dataset.

Input: Space separated string, contains only characters a-z and spaces.
Assume also that all data is available at start of program execution,
and can be read once and interrogated many times. Sequence of
observations could be very long (but assume it's short enough to be able
to fit into memory).

Lots of complications, so list any assumptions.
List points for future work
Testing
Indicate complexity if known

e.g.
Input: red red blue red
Params: red, blue
Output: 1

Input: yellow yellow blue yellow yellow red
Params: red blue
Output: 3

Strategy:
- Assume you know all possible colours a car can take
- Examine first colour, check if you've examined it before,
    - if not, then c
"""

POSSIBLE_COLOURS = {'r', 'b'}

DATA_STREAM = 'b b b r r r'


def min_distance(c1, c2, data=None, examined_colours=None, distance=0):

    if len(data) == 0 or examined_colours == POSSIBLE_COLOURS:
        return distance

    if not data:
        data = DATA_STREAM.split(' ')

    if not examined_colours:
        examined_colours = set()

    current_colour = data[0]

    if current_colour not in examined_colours:
        examined_colours.add(current_colour)

    for idx, c in enumerate(data[1:]):
        if c not in examined_colours:
            examined_colours.add(c)
            distance += idx

    return min_distance(c1, c2, data[1:], examined_colours, distance)


if __name__ == "__main__":
    print(min_distance(1, 2, DATA_STREAM.split(' ')))