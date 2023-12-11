import math

class Vehicle:
    def __init__(self, radius: float, theta: float) -> None:
        self._radius = radius
        self._theta = theta 
        self._heading = math.radians(90)

        # Print initial position and heading
        x, y = self._polar_to_cartesian(radius, theta)
        print(f"Initial position: ({round(x, 2)}, {round(y, 2)}). Heading: {math.degrees(self._heading)}°.")

    # ############################################################
    # PROTECTED METHODS
    # ############################################################
    def _polar_to_cartesian(self, radius: float, theta: float) -> tuple:
        """Converts polar coordinates to cartesian coordinates."""
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        return x, y

    # ############################################################
    # PUBLIC METHODS
    # ############################################################
    def move(self, distance: float = 1) -> None:
        """Moves the vehicle a specified distance along the current heading."""
        x1, y1 = self._polar_to_cartesian(self._radius, self._theta)
        x2, y2 = self._polar_to_cartesian(distance, self._heading)
        x3 = x1 + x2
        y3 = y1 + y2

        self._radius = math.sqrt(x3**2 + y3**2)
        self._theta = math.atan2(y3, x3)
        print(f"Moving {distance} units. New position: ({round(x3, 2)}, {round(y3, 2)}).")

    def turn_left(self) -> None:
        """Turns the vehicle 90 degrees to the left."""
        self._heading = (self._heading + math.pi / 2) % (2 * math.pi)
        print( f"Turning left. New heading: {math.degrees(self._heading)}°.")

    def turn_right(self) -> None:
        """Turns the vehicle 90 degrees to the right."""
        self._heading = (self._heading - math.pi / 2) % (2 * math.pi)
        print( f"Turning right. New heading: {math.degrees(self._heading)}°.")

# Example Usage:
vehicle = Vehicle(0, 0)
vehicle.turn_left()
vehicle.move(1)
vehicle.turn_right()
vehicle.move(2)
vehicle.turn_right()
vehicle.move(1)