import random

import pygame

class Particle():
    def __init__(self, placement):
        self.placement = placement # [mx, my]
        self.radius = random.randint(4,6)
        self.velocity = [random.randint(0, 7) - 3.5, random.randint(0, 7) - 3.5]

    def render(self, screen):
        pygame.draw.circle(
            screen,
            pygame.Color('white'),
            (int(self.placement[0]), int(self.placement[1])),
            int(self.radius)
        )

    def update(self):
        self.placement[0] += self.velocity[0]
        self.placement[1] += self.velocity[1]

        self.velocity[1] += 0.1 #gravity
        self.radius -= 0.1

class Particles():
    def __init__(self):
        self.particles = []

    def spawn(self, location):
        self.particles.append(Particle(location))

    def render(self, screen):
        for particle in self.particles:
            particle.render(screen)

    def update(self):
        # work with the list in reverse order so we can safely remove items while iterating
        for i, particle in sorted(enumerate(self.particles), reverse=True):
            particle.update()

            if particle.radius <= 0:
                self.particles.pop(i)