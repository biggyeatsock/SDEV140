class Car:
    # ############################################################
    # CONSTRUCTOR
    # ############################################################
    def __init__(
            self, 
            heading: str = 'N', 
            x: float = 0.0, 
            y: float = 0.0, 
        ) -> None:
        # ############################################################
        # PROTECTED ATTRIBUTES
        # ############################################################
        # This dictionary maps the heading index to the heading string.
        # It allows us to simplify the logic of the turn_left() and turn_right() methods.
        self._DIRECTIONS = { 0: 'N', 1: 'E', 2: 'S', 3: 'W' }

        # Direction that the car is facing.
        self._heading = self.__get_heading_index_from_string(heading)

        # X and Y coordinates for the car.
        self._x = x
        self._y = y

        # km / minute
        self._velocity = 1.0

        # Give some friendly output to the user.
        print(f"Initial position: ({self._x}, {self._y}). Initial heading: {self._DIRECTIONS[self._heading]}.")


    # ############################################################
    # PRIVATE METHODS
    # ############################################################
    def __get_heading_index_from_string(self, heading: str) -> int:
        """Validates the heading passed to the constructor."""
        # Sanitize the user input.
        heading = heading.upper().strip()

        # Check to see if the heading is in the dictionary.
        if heading not in self._DIRECTIONS.values():
            raise ValueError(f"Invalid heading: {heading}. Valid headings are: {', '.join(self._DIRECTIONS.values())}")

        # Loop through the dictionary and return the index of the heading.
        for index, direction in self._DIRECTIONS.items():
            if direction == heading:
                return index

        # We should really raise an exception here, but we'll just return None for now.
        return None

    # ############################################################
    # PUBLIC METHODS
    # ############################################################
    def move(self, time: float = 1.0) -> None:
        """Moves the vehicle forward a specified time."""
        distance = time * self._velocity
        if self._heading == 0:
            self._y += distance
        elif self._heading == 1:
            self._x += distance
        elif self._heading == 2:
            self._y -= distance
        elif self._heading == 3:
            self._x -= distance

        print(f"Accelerating for {time} minutes. New position: ({round(self._x, 2)}, {round(self._y, 2)}).")
        pass

    def turn_left(self) -> None:
        """Turns the vehicle 90 degrees to the left."""
        self._heading = (self._heading - 1) % 4
        print( f"Turning left. New heading: {self._DIRECTIONS[self._heading]}.")
        pass

    def turn_right(self) -> None:
        """Turns the vehicle 90 degrees to the right."""
        self._heading = (self._heading + 1) % 4
        print( f"Turning right. New heading: {self._DIRECTIONS[self._heading]}.")

# Example Usage:
# car = Car()
# car.turn_right()
# car.move(1)
# car.turn_left()
# car.move(1)

# car2 = Car(heading='W', x=5, y=5)
# car2.move(5)