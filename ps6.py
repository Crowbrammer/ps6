# This Python file uses the following encoding: utf-8

# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.clean_tile_dict = dict()
        # self.width = width
        # self.height = height
        for cur_width in range(width):
            for cur_height in range(height):
                self.clean_tile_dict[(cur_width, cur_height)] = "dirty"
        return

        #raise NotImplementedError

    def getRoomWidth(self):
        """
        Returns room's width
        """
        return self.width

    def getRoomHeight(self):
        """
        Returns room's height
        """
        return self.height

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        int_pos_x = int(pos.getX())
        int_pos_y = int(pos.getY())
        self.clean_tile_dict[int_pos_x, int_pos_y] = "clean"
        return
        #raise NotImplementedError

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.clean_tile_dict[(m, n)] == "clean"
        #raise NotImplementedError

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """

        return float(len(self.clean_tile_dict.items()))
        # raise NotImplementedError

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """

        return float(self.clean_tile_dict.values().count("clean"))

        #for x in self.

        # return sum(self.clean_tile_dict.values)
        # ^^^ Only works with the True/False methodology
        # while True:
        #     try:
        #         clean_tiles = [x for x in self.clean_tile_dict.values()]
        #         clean_tiles.remove("dirty")
        #     except ValueError:
        #         break
        #     except AttributeError:
        #         pass
        # raise NotImplementedError

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        pos = Position(random.random() * self.getRoomWidth(), random.random() * self.getRoomHeight())
        return pos
        # raise NotImplementedError

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return 0 <= pos.getX() < self.getRoomWidth() and 0 <= pos.getY() < self.getRoomHeight()
        # raise NotImplementedError


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = round(speed, 3)
        self.pos = Position(random.random() * room.width, random.random() * room.height)
        self.direction = int(random.random() * 360)
        # raise NotImplementedError

    def getRobotRoom(self):
        """
        Returns the room the robot's in. Primarily to use the getRandomPosition
        functionality.
        """
        return self.room

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
        # raise NotImplementedError

    def getRobotSpeed(self):
        """
        Return the speed of the robot.

        returns: the robot's speed attribute
        """
        return self.speed

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
        #raise NotImplementedError

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position
        self.getRobotRoom().cleanTileAtPosition(position)
        return
        # raise NotImplementedError

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
        return
        #raise NotImplementedError

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #return Position().getNewPosition(self.getRobotDirection, self.speed)
        raise NotImplementedError


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        # def positionWork(x, y):
        #     self.setRobotPosition(x, y)
        # new_direction = int(random.random() * 360)
        #self.setRobotDirection(new_direction)
        self.setRobotPosition(self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.getRobotSpeed()))

        my_room = self.getRobotRoom()
        my_pos = self.getRobotPosition()
        new_pos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.getRobotSpeed())
        #for each in range(6):
            #print(my_room.isPositionInRoom(new_pos))

        if my_room.isPositionInRoom(new_pos) != True:
            new_direction = int(random.random() * 360)
            self.setRobotDirection(new_direction)

            if new_pos.getX() > my_room.width and new_pos.getY() > my_room.height:
                new_pos = Position(my_room.width, my_room.height)
                self.setRobotPosition(new_pos)
            elif new_pos.getX() < my_room.width and new_pos.getY() < my_room.height:
                new_pos = Position(0, 0)
                self.setRobotPosition(new_pos)
            elif new_pos.getX() > my_room.width:
                new_pos = Position(my_room.width, new_pos.getY())
                self.setRobotPosition(new_pos)
            elif new_pos.getY() > my_room.height:
                new_pos = Position(new_pos.getY(), my_room.height)
                self.setRobotPosition(new_pos)
        else:
            self.setRobotPosition(new_pos)

            #new_pos = new_pos.getNewPosition(self.getRobotDirection(), self.getRobotSpeed())
        #new_direction = int(random.random() * 360)
        #self.setRobotPosition(new_pos)
        #self.setRobotPosition(self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.getRobotSpeed()))
        my_room.cleanTileAtPosition(my_pos)
        # raise NotImplementedError

# === Problem 3



def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)

    The main issue is that you define robots with the room already there. And the room is what...
    Wait, I got it. Don't use the parentheses, except within the function. Yay! That was useful
    to think about!!!
    """

    # Some ground rules for the party
    assert num_robots > 0, "Please set the number of robots to at least one."
    assert speed > 0, "Please set a speed greater than 0."
    assert width > 0 and height > 0, "Please make width and height are greater than 0."
    assert min_coverage > 0 <= 1.0, "Please set min_coverage to between 0 and 1, inclusive."
    assert num_trials, "Please set num_trials to at least one"


    trial_results = []

    # Run the trials. This will probably bug out at first.
    for trial in range(num_trials):
        # We're going to clean Jimmy's place, after the party
        jimmys_place = RectangularRoom(width, height)

        # Unleash the robots into Jimmy's place
        robots_in_jimmys = []
        for each in range(num_robots):
            robots_in_jimmys.append(robot_type(jimmys_place, speed))
        # print(robots_in_jimmys)
        anim = ps6_visualize.RobotVisualization(num_robots, width, height)
        for this_robot in robots_in_jimmys:
            this_robot.setRobotPosition(jimmys_place.getRandomPosition())
        clock_ticks = 0
        while jimmys_place.getNumCleanedTiles() / jimmys_place.getNumTiles() < min_coverage:
            # print(jimmys_place.getNumCleanedTiles() / jimmys_place.getNumTiles())
            for this_robot in robots_in_jimmys:
                this_robot.updatePositionAndClean()
                anim.update(jimmys_place, robots_in_jimmys)
            clock_ticks += 1
        anim.update(jimmys_place, robots_in_jimmys)
        # print(trial_results)

        trial_results.append(clock_ticks)


    average_finish_time = sum(trial_results) / len(trial_results)

    return "{} robot(s) takes around {} clock ticks to completely clean a {} by {} room, \
            on average from {} trials.".format( \
            num_robots, average_finish_time, width, height, num_trials)
    # raise NotImplementedError

print(runSimulation(num_robots=1, speed=1.0, width=5, height=5, min_coverage=1.0, num_trials=1000,
                  robot_type=StandardRobot))



# === Problem 4
#
# 1) How long does it take to clean 80% of a 20�20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions
#	 20�20, 25�16, 40�10, 50�8, 80�5, and 100�4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    raise NotImplementedError

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    raise NotImplementedError

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    raise NotImplementedError


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    raise NotImplementedError
