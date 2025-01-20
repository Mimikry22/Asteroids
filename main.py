import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots,updatable,drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        for obj in updatable:
             obj.update(dt)

        for asteroid in asteroids:
             if asteroid.check_for_collision(player):
                  print("Game over!")
                  sys.exit()

        for asteroid in asteroids:
             for bullet in shots:
                  if asteroid.check_for_collision(bullet):
                       asteroid.split()
                       bullet.kill()

        screen.fill('black')

        for obj in drawable:
             obj.draw(screen)

        pygame.display.flip()
        dt_time = clock.tick(60)
        dt = dt_time/1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()
        