import random

import pygame

class Particle():
    def __init__(self, placement):
        self._placement = placement # [mx, my]
        self._radius = random.randint(4,6)
        self._velocity = [random.randint(0, 7) - 3.5, random.randint(0, 7) - 3.5]

    def burned_out(self):
        return self._radius <= 0

    def render(self, screen):
        pygame.draw.circle(
            screen,
            pygame.Color('white'),
            (int(self._placement[0]), int(self._placement[1])),
            int(self._radius)
        )

    def update(self):
        self._placement[0] += self._velocity[0]
        self._placement[1] += self._velocity[1]

        self._velocity[1] += 0.1 #gravity
        self._radius -= 0.1

class Particles():
    def __init__(self):
        self._particles = []

    def spawn(self, location):
        self._particles.append(Particle(location))

    def render(self, screen):
        for particle in self._particles:
            particle.render(screen)

    def update(self):
        # work with the list in reverse order so we can safely remove items while iterating
        for i, particle in sorted(enumerate(self._particles), reverse=True):
            particle.update()

            if particle.burned_out():
                self._particles.pop(i)