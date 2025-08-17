import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
       

    def draw(self, screen):
        pygame.draw.circle(screen,color="white", center=self.position, radius=SHOT_RADIUS, width=2) #or surface = screen?

    def update(self, dt):
        self.position += self.velocity * dt