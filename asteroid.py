import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Initialize any asteroid-specific properties here

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
    # Override the update() method so that it moves in a straight line at constant speed. 
    # On each frame, it should add (self.velocity * dt) to its position (get self.velocity 
    # from its parent class, CircleShape).

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        first_split_vector = self.velocity.rotate(angle) * 1.2
        second_split_vector = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_split_vector
        second_asteroid.velocity = second_split_vector


