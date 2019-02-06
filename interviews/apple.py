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
"""


DATA_STREAM = 'a o b c d b x a end'

DATA_STREAM = 'y y b y y r end'


def start_point(c, data):
    """Generate the starting point of the algorithm"""
    for idx, value in enumerate(data):
        if value == c:
            yield idx+1, data[idx+1:]


def min_distance(c1, c2, data):
    """Find the minimum distance"""
    if c1 == c2:
        return 0

    distances = []
    for idx, dat in start_point(c1, data):
        forward = dat
        backward = list(reversed(data[:idx-1]))

        forward_dist = 0
        for idx, c in enumerate(forward):
            if idx == len(forward)-1:  # end of list without finding
                forward_dist = 1000000  # some very large distance
                distances.append(forward_dist)
            else:
                forward_dist += 1
                if c == c2:
                    distances.append(forward_dist)
                    break

        backward_dist = 0
        for c in backward:
            if idx == len(backward)-1:
                backward_dist = 1000000
                distances.append(backward_dist)
            else:
                backward_dist += 1
                if c == c2:
                    distances.append(backward_dist)
                    break

    return min(distances)


if __name__ == "__main__":
    data = DATA_STREAM.split((' '))
    c1 = 'r'
    c2 = 'b'
    print("Input data \n", data)
    print("min distance between '{}' and '{}' is {}".format(c1, c2, min_distance(c1, c2, data)))

