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

Assumptions:
- Assume you know all possible colours a car can take in a given data set,
and can't query or colours other than these
- Assume that the end of the data set can be marked with a sentinel
- Assume that there are no spelling errors in the data set, and a given
string will be read without any special parsing, explicitly
- Assume
- Assume that there is some arbitrarily large maximum distance possible
between cars.
- Assume

TODO:
- Complexity analysis
"""


def sub_array_generator(colour, colour_data):
    """
    Generate the left and right sub arrays for a given colour of the
    algorithm, yielding sub arrays from subsequent occurrences of the
    same colour.

    :param str colour: The colour being searched for.
    :param list[str] colour_data: The data set containing the colour of
    each car.
    :returns tuple[list[str], list[str]]: The left and right sub arrays
    from a given colour. Yield left sub array in reverse order.
    """
    for idx, c in enumerate(colour_data):
        if c == colour:
            yield colour_data[idx+1:], list(reversed(colour_data[:idx]))


def min_distance(colour_1, colour_2, colour_data):
    """
    Find the minimum distance between two cars of specified colours in
    some data.
    :param str colour_1: The colour of the first car.
    :param str colour_2: The colour of the second car.
    :param list[str] colour_data: The data set containing the colours of
    all the cars
    :return int: The minimum distance between cars of colour_1 and
    colour_2.
    """
    max_distance = 1e6

    if colour_1 == colour_2:
        return 0

    distances = []

    for r_sub_array, l_sub_array in sub_array_generator(colour_1, colour_data):

        sub_arrays = [r_sub_array, l_sub_array]

        for sub_array in sub_arrays:
            distance = 0
            for idx, colour in enumerate(sub_array):
                # Reached end of sub array without finding colour_2
                if idx == len(sub_array) - 1:
                    # Set to some arbitrarily large distance
                    distances.append(max_distance)

                distance += 1
                if colour == colour_2:
                    # Don't loop any further if we found min distance
                    if distance == 1:
                        return distance
                    distances.append(distance)
                    break

    if not distances:
        raise ValueError(
            'Queried data set with unsupported colours',
            colour_1,
            colour_2
        )

    return min(distances)


if __name__ == "__main__":
    data_stream = 'red orange blue green yellow blue green red end'
    data = data_stream.split((' '))
    c1 = 'orange'
    c2 = 'red'

    print("Input data \n", data)
    print(
        "Minimum distance between '{}' and '{}' is {}".format(
            c1,
            c2,
            min_distance(c1, c2, data)
        )
    )

