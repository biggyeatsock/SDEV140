from car import Car
from rocketcar import RocketCar

# car = Car(heading = 'N', x=0, y=0)
# car.move()
# car.turn_left()
# car.move(1)
# car.turn_left()
# car.move(1)
# car.turn_left()
# car.move(1)



rocket_car = RocketCar(heading='N', x=0, y=0, fuel=2)

rocket_car.move(1)
rocket_car.toggle_rocket_fuel()
rocket_car.move(5)
