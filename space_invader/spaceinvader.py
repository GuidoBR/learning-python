import pygame
from pygame.locals import *
import sys

class SpaceInvaders:
    def __init__(self):
        self.screen = pygame.display._set_mode(800, 600)
        self.enemy = [pygame.image('assets/a1_0.png').convert(), pygame.image('assets/a1_1.png').convert()]
        self.animationOn = 0

    def enemyUpdate(self):
        pass

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.screen.fill(0, 0, 0)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == "__main__":
    SpaceInvaders().run()
