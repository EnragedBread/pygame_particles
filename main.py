import random

import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN

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
                    vx = random.randint(0, 7) - 3.5
                    vy = random.randint(0, 7) - 3.5
                    radius = random.randint(4,6)
                    particles.append([[mx, my], radius, [vx, vy]])

        # UPDATE
        # work with the list in reverse order so we can safely remove items while iterating
        for i, particle in sorted(enumerate(particles), reverse=True):
            particle[0][0] += particle[2][0]
            particle[0][1] += particle[2][1]

            particle[2][1] += 0.1 #gravity
            particle[1] -= 0.1

            if particle[1] <= 0:
                particles.pop(i)

        # RENDER
        screen.fill(pygame.Color('black'))
        for particle in particles:
            pygame.draw.circle(
                screen,
                pygame.Color('white'),
                (int(particle[0][0]), int(particle[0][1])),
                int(particle[1])
            )

        pygame.display.flip()

if __name__ == '__main__':
    main()