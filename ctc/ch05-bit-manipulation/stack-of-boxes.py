"""
You have a stack of n boxes with width w_i, heigts h_i, and depths d_i.
    The boxes can't be rotated, and can only be stacked on top of one
    another if each box in the stack is strictly larger than the box
    above it in width, height and depth.

Implement a method to compute the tallest possible height of a stack.

Strategy:
    - if previous box see if this is bigger than it, if it is, remove
    previous box, and place this one underneath.
    - If there isn't a previous box, place this box at bottom.
    - Do this until you've placed all of the boxes on top of one another
"""


class Box:

    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

    def __repr__(self):
        return str(
            {
                "w": self.w,
                "h": self.h,
                "d": self.d,
            }
        )

    def __getitem__(self, item):
        return self.__dict__[item]


BOXES = [Box(i, i, i) for i in range(1, 10)]


def can_stack(box_a, box_b):
    if box_a.w > box_b.w and box_a.h > box_b.h and box_a.d > box_b.d:
        return True
    return False


def can_place_below(box_a, box_b):
    if box_a.w < box_b.w and box_a.h < box_b.h and box_a.d < box_b.d:
        return True
    return False


def tallest_height(i, boxes, order=None, n_boxes=None):

    curr = boxes[i]

    if not isinstance(order, list):
        order = [curr]

    if not isinstance(n_boxes, int):
        n_boxes = len(boxes)

    if i >= n_boxes-1:
        return sum([b['d'] for b in order])

    for idx, box in enumerate(order):
        if can_stack(curr, box) or can_place_below(curr, box):
            order.insert(idx, curr)
            break
        else:
            pass

    tallest_height(i+1, boxes, order, n_boxes)

    return sum([b['d'] for b in order])


if __name__ == "__main__":
    b = [Box(3, 3, 3), Box(2, 2, 2), Box(1, 10, 1), Box(0, 0, 0)]
    print(b)

    print(tallest_height(0, b))