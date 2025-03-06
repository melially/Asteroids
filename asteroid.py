import pygame
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