import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,color="white", center=self.position, radius=self.radius , width=2) #or surface = screen?

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            rotate_angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(rotate_angle)
            vector_2 = self.velocity.rotate(-rotate_angle)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, self.new_radius) #self.position = self.position.x, self.position.y to extraxt X and y from vector
            new_asteroid2 = Asteroid(self.position.x, self.position.y, self.new_radius)
            new_asteroid1.velocity = vector_1 * 1.2
            new_asteroid2.velocity = vector_2 * 1.2
       


