import pygame
import time
from Pendulum import Pendulum
from LinearMovement import LinearMovement

class PendulumSystem:
    def __init__(self, pendulum_length, pendulum_mass):
        self.pendulum = Pendulum(pendulum_length, pendulum_mass, (255, 255, 255))
        self.linear_movement = LinearMovement(400, 200, 600)

    def update(self, dt, x):
        self.linear_movement.move_to_x(x)
        self.linear_movement.update(dt)
        v = self.linear_movement.get_velocity()
        self.pendulum.update(dt, v)

    def draw(self, surface, y):
        x = self.linear_movement.get_x()
        self.pendulum.draw(surface, x, y)

if __name__ == "__main__":
    pygame.init()

    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    PENDULUM_LENGTH = 200
    PENDULUM_MASS = 1
    
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pendulum = PendulumSystem(PENDULUM_LENGTH, PENDULUM_MASS)
    last_time = time.time()
    x = 0

    while running:
        current_time = time.time()
        dt = (current_time - last_time) * 10 # diif in time since last fram * 10
        
        last_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
            pygame.quit()
        mouse_x = pygame.mouse.get_pos()[0]
        if 200 < mouse_x < 600:
            x = mouse_x

        pendulum.update(dt, x)
        screen.fill((0, 0, 0))  # Clear the screen
        pygame.draw.rect(screen, (120, 0, 0), pygame.Rect(0, 200, SCREEN_WIDTH, 100))
        pygame.draw.rect(screen, (20, 0, 0), pygame.Rect(180, 240, 440, 20))
        pendulum.draw(screen, 250)

        pygame.display.flip()

    pygame.quit()
