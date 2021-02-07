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
