import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, shots):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            print(f"Rotating left. Current rotation: {self.rotation}")
        if keys[pygame.K_d]:
            self.rotate(dt)
            print(f"Rotating right. Current rotation: {self.rotation}")
        if keys[pygame.K_w]:
            self.move(dt)
            print(f"Moving forward. Current move: {self.position}")
        if keys[pygame.K_s]:
            self.move(-dt)
            print(f"Moving backward. Current rotation: {self.position}")
        if keys[pygame.K_SPACE]:
            self.shoot()
            print(f"Shot fired from: {self.position}")

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.shots.add(shot)
            self.timer += PLAYER_SHOOT_COOLDOWN

        # Create new shot at player position
        # Set its velocity