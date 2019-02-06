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
- Assume you know all possible colours a car can take in a given dataset,
and can't query or colours other than these
"""


DATA_STREAM = 'a o b a d b x r end'


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

        directions = [forward, backward]

        for direction in directions:
            distance = 0
            for idx, c in enumerate(direction):
                if idx == len(direction) - 1:  # end of list without finding
                    distance = 1000000  # some very large distance
                    distances.append(distance)
                else:
                    distance += 1
                    if c == c2:
                        if distance == 1:  # dont loop any further if we found min distance
                            return distance
                        distances.append(distance)
                        break

    return min(distances)


if __name__ == "__main__":
    data = DATA_STREAM.split((' '))
    c1 = 'r'
    c2 = 'b'
    print("Input data \n", data)
    print("min distance between '{}' and '{}' is {}".format(c1, c2, min_distance(c1, c2, data)))

