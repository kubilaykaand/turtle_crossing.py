import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# how to call random and turtle as a superclass in one class
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.probability_assigner = 6
        self.increase_cars_per_10_levels = 1

    def create_car(self):
        self.random_chance = random.randint(1, self.probability_assigner)
        if self.random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    def increase_the_speed(self):
        self.car_speed = self.car_speed+MOVE_INCREMENT
        self.increase_cars_per_10_levels += 1
        if self.increase_cars_per_10_levels % 10==0:
            self.probability_assigner -= 1
            if self.probability_assigner <=2:
                self.probability_assigner=2
    #once in every 10 levels, the probability of a car spawn is increased
    #by decreasing the random number generator cap(highest) value, yet those options can be tweaked depending
    #on the MOVE_INCREMENT values, and the RNG option. (This was needed due to the increased speeds will
    #make the cars look spawn lesser.

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
