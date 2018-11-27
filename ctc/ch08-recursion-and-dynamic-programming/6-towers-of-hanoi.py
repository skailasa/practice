"""
Classic
- 3 towers, and N disks of different sizes which can be slid onto a
    tower.
- The puzzle starts with disks sorted in ascending order of size from
    top to bottom, i.e. each disk sits on top of a larger one.
- Following constraints:
    (i) Only one disk can be moved at a time
    (ii) A disk is slid off the top of one tower onto another tower
    (iii) A disk cannot be placed on top of a smaller disk.

Write a program to move the disks from the first to last tower using
    stacks.
"""


def hanoi(n, source, helper, target):
    print("hanoi( ", n, source, helper, target, " called")
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)

        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            print("moving " + str(disk) + " from " + source[1] + " to " + target[1])
            target[0].append(disk)

        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)


if __name__ == "__main__":
    source = ([2, 1], "source")
    target = ([], "target")
    helper = ([], "helper")
    hanoi(len(source[0]), source, helper, target)

    print(source, helper, target)