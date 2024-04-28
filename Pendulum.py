import pygame
from math import sin, cos, pi

class Pendulum:
    def __init__(self, length, mass, color):
        """
        Initialize Pendulum object.

        Args:
            length (float): Length of the pendulum.
            mass (float): Mass of the pendulum bob.
            color (tuple): RGB color tuple for drawing the pendulum.
        """
        self.length = length
        self.mass = mass
        self.color = color
        self.angle = pi / 4  # Initial angle (45 degrees)
        self.angular_velocity = 0  # Initial angular velocity
        self.angular_acceleration = 0  # Initial angular acceleration
    
    def update(self, dt, v):
        """
        Update the state of the pendulum.

        Args:
            dt (float): Time elapsed since last update.
            v (float): Linear velocity of the pendulum bob.
        """
        gravity = -9.81  # m/s^2
        friction_coefficient = 0.60
        torque = gravity * self.mass * self.length * sin(self.angle) - friction_coefficient * self.angular_velocity
        moment_of_inertia = self.mass * self.length ** 2
        self.angular_acceleration = torque / moment_of_inertia
        self.angular_velocity += self.angular_acceleration * dt
        self.angle += self.angular_velocity * dt
        dx = v * dt
        self.angle -= dx / self.length
        self.angle %= 2 * pi #angle never more than 360


    def draw(self, surface, x, y):
        """
        Draw the pendulum on the given surface.

        Args:
            surface: Pygame surface to draw the pendulum on.
            x (int): X-coordinate of the pivot point.
            y (int): Y-coordinate of the pivot point.
        """
        # Calculate position of pendulum bob
        bob_x = x + self.length * sin(self.angle)
        bob_y = y + self.length * cos(self.angle)
        pygame.draw.line(surface, self.color, (x, y), (bob_x, bob_y), 4)  # Rod
        pygame.draw.circle(surface, self.color, (int(bob_x), int(bob_y)), 10)  # Bob

    def get_angle(self):
        """
        Get the current angle of the pendulum.
        """
        return self.angle
