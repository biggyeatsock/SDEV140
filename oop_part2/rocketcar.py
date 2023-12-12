from car import Car

class RocketCar(Car):
    def __init__(self, 
            heading: str = 'N', 
            x: float = 0.0, 
            y: float = 0.0, 
            fuel : float = 2
            )-> None :
        
            #called the constructor from car
            super().__init__(heading, x=x, y=y)

            self._BASE_VELOCITY = 2
            self._ROCKET_VELOCITY = 10
            self._use_rocket_fuel = False
            self._minutes_of_fuel = 2.0

            # RocketCar is much faster than a car
            #Km / minute
            self._velocity = 2.0

    def toggle_rocket_fuel(self):
        self._use_rocket_fuel = not self._use_rocket_fuel
        if self._use_rocket_fuel:
            print('ROcket fuel is now on!')
            self._velocity = self._ROCKET_VELOCITY
        else:
            self._velocity = self._BASE_VELOCITY
    
    def move(self, time:float = 1) -> None:
        if self._use_rocket_fuel:
            fueled_move = 0.0
            unfueled_move = time
            # First we got to figure out if we have enough fuel
            fueled_move = min(self._minutes_of_fuel, time)
            unfueled_move = time - fueled_move

            #updating the fuel level
            self._minutes_of_fuel -= fueled_move

            # Move (With the rocket fuel)
            super().move(fueled_move)

            if fueled_move < time:
                print('Rocket fuel ran out!')
                self.toggle_rocket_fuel()
                super().move(unfueled_move)
        else:
            super().move(time)