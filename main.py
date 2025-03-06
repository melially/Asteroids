import pygame # this allows us to use code from the open-source pygame library throughout this file
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            print("Key A is pressed")
        if keys[pygame.K_d]:
            print("Key D is pressed")
        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(f"Delta time (dt): {dt}")

if __name__ == "__main__":
    main()