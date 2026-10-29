import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)


if __name__ == "__main__":
    main()
