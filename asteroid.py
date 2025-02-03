import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        print(f"Creating asteroid at {x}, {y} with radius {radius}")
    
    def draw(self, screen):
        pygame.draw.circle(screen,(0,255,255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            vector1 = pygame.math.Vector2(self.velocity).rotate(random_angle)
            vector2 = pygame.math.Vector2(self.velocity).rotate(-random_angle)
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = vector1 * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = vector2 * 1.2



