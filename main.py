import random

import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN

from particle import Particle

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('particles demo')
    clock = pygame.time.Clock()
    particles = [] #placement, radius, velocity

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                return
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                for i in range(10):
                    particles.append(Particle([mx, my]))

        # UPDATE
        # work with the list in reverse order so we can safely remove items while iterating
        for i, particle in sorted(enumerate(particles), reverse=True):
            particle.update()

            if particle.radius <= 0:
                particles.pop(i)

        # RENDER
        screen.fill(pygame.Color('black'))

        for particle in particles:
            particle.render(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()