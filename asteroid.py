import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,color="white", center=self.position, radius=PLAYER_RADIUS, width=2) #or surface = screen?

    def update(self, dt):
        self.position += self.velocity * dt