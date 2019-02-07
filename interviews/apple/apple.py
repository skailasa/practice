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

e.g.
Input: red red blue red
Params: red, blue
Output: 1

Input: yellow yellow blue yellow yellow red
Params: red blue
Output: 3

Strategy:
Loop through array to find colour1, from here loop forwards and
backwards looking for colour2 storing the resulting distances. Repeat
until all distances have been found, calculate minimum.

Assumptions:
- Assume you know all possible colours a car can take in a given data
set, and can't query or colours other than these.
- Assume that the end of the data set can be marked with a sentinel.
- Assume that there are no spelling errors in the data set, and a given
string will be read without any special parsing, explicitly.
- Assume that there is some arbitrarily large maximum distance possible
between cars.
- Assume all car colours are evenly distributed.

Space Complexity Analysis:
My solution operates on the data in-place, but my min distance
calculation, is removable, instead one should just store a calculated
distance if it is smaller than a cached 'current smallest distance'.

Time Complexity Analysis:
My solution is really just a nested loop:

Outer Loop: loop through all possible points where we start with colour1.
    Call this a 'start point'.
    Inner Loop 1: loop forward from each start point to find colour2
    Inner Loop 2: loop backward from each start point to find colour2
    Store distances.
    Calculate minimum distance

In the worst case all colour1's are close to the middle, and colour 2 is
located at beginning AND end of a given data set.

e.g.
colour1 = 'red'
colour2 = 'blue'

'blue x x x x red x x x x blue'

In which case my algorithm will run in O(N(A+B)) = O(N^2), which we
can use as an upper bound. Where N is the number of elements in the data
set, and A and B are the length of the inner loops respectively. Even
if there more occurrences of 'red' in the above example, the asymptotic
complexity would be the same.

This is because at the moment my algorithm finds the distances between
all pairs of colour1 and colour2 to exhaustion, so in this scenario will
have to iterate through the entire list for each start point.

However, in the best case colour1 is at the beginning of the data set,
with colour2 adjacent to it, the min possible distance, giving O(1).

It's difficult to perform any analysis for how this amortizes without
knowledge of the distribution of car colours. Operating under the
assumption that all car colours are evenly distributed, we would again
get O(N(A+B)) asymptotic time complexity, as the fundamental algorithm
is still a nested loop.

Improvements to Algorithm/Implementation:
The runtime complexity faces the bottleneck of nested loop, however
looping over the forward running, and backward running sub arrays is
trivially parallelisable as they don't depend on each other at all.
This won't change the complexity, but would speed up computation.

Instead of exhaustively looking for all the distances an improvement
to the algorithm would be to break the inner loop if a distance is
greater than a cached 'current smallest distance', however I do not
have enough time to improve my implementation.
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
            colour_2,
        )

    return min(distances)
