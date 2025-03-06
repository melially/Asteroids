import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision_det(self, other_object):
        distance = self.position.distance_to(other_object.position)     # Calculate the actual distance between centers

        collision_distance = self.radius + other_object.radius     # Calculate the minimum distance before collision occurs

        return distance <= collision_distance
        
        # center = self.position
        # centerOther = other_object.position

        # max_dist_square = (self.radius + other_object.radius) ** 2
        # return center.distance_squared_to(centerOther) < max_dist_square # True or false