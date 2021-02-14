import random

import pygame
from pygame.math import Vector2

class Particle():
    def __init__(self, placement):
        self._placement = Vector2(placement)
        self._radius = random.randint(4,6)
        self._velocity = Vector2((random.randint(0, 7) - 3.5, random.randint(0, 7) - 3.5))

    def burned_out(self):
        return self._radius <= 0

    def render(self, screen):
        pygame.draw.circle(
            screen,
            pygame.Color('white'),
            (int(self._placement.x), int(self._placement.y)),
            int(self._radius)
        )

    def update(self):
        self._placement += self._velocity

        self._velocity.y += 0.1 #gravity
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