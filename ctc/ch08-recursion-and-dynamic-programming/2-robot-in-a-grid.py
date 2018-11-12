"""
Imagine a robot sitting on the upper left hand corner of a grid with r rows
and c columns.
The robot can only move in two directions right and down, but certain cells are
off limits such that the robot can't step on them.
Design an algorithm to find a path for the robot from the top left to the bottom
right.
"""


class Robot:

    def __init__(self, c, r, dead_positions):
        self.current_position = (c, r)
        self.dead_positions = dead_positions

    def can_move_left(self):
        potential_position = self.current_position[0]-1, self.current_position[1]

        if potential_position[0] >= 0 and potential_position not in self.dead_positions:
            return True
        return False

    def move_left(self):
        if self.can_move_left():
            self.current_position = self.current_position[0]-1, self.current_position[1]

    def can_move_up(self):
        potential_position = self.current_position[0], self.current_position[1]-1

        if potential_position[1] >= 0 and potential_position not in self.dead_positions:
            return True
        return False

    def move_up(self):
        if self.can_move_up():
            self.current_position = self.current_position[0], self.current_position[1]-1


class Grid:

    def __init__(self, c, r):
        self._c = c
        self._r = r
        self._path = [(c, r)]

    @property
    def initial_position(self):
        return self._c, self._r

    @property
    def path(self):
        return self._path[::-1]

    def find_path(self, robot):
        """
        Recursively find the path the robot took through the grid
        """
        top_left = (0, 0)

        if robot.current_position == top_left:
            return

        else:
            robot.move_left()
            self._path.append(robot.current_position)

            robot.move_up()
            self._path.append(robot.current_position)

        self.find_path(robot)



if __name__ == "__main__":
    r = Robot(2, 2, [(1,1)])

    g = Grid(2, 2)

    g.find_path(r)

    print(g.path)

