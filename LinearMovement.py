import enum
class LinearMovement:
    def __init__(self, initial_x, min_x, max_x):
        """
        Initialize LinearMovement object.

        Args:
            initial_x (float): Initial position.
            min_x (float): Minimum allowed position.
            max_x (float): Maximum allowed position.
        """
        self.current_x = initial_x
        self.velocity = 0
        self.acceleration = 10
        self.max_x = max_x
        self.min_x = min_x
        self.target_x = None
        self.direction = Direction.STATIONARY

    def update(self, dt):
        """
        Update position and velocity based on time elapsed.

        Args:
            dt (float): Time elapsed since last update.
        """
        # Update position based on velocity and acceleration
        self.current_x += self.velocity * dt + 0.5 * self.acceleration * dt**2 * self.direction.value
        # Check if the goal position is reached or overshot
        if self.target_x is not None:
            if (self.direction == Direction.POSITIVE and self.current_x >= self.target_x) or \
               (self.direction ==Direction.NEGATIVE and self.current_x <= self.target_x):
                # Stop at the goal position
                self.current_x = self.target_x
                self.velocity = 0
                self.target_x = None
                self.direction = Direction.STATIONARY
        # Apply limits to x position
        self.current_x = max(self.min_x, min(self.current_x, self.max_x))

        # Update velocity based on acceleration
        self.velocity += self.acceleration * dt * self.direction.value

    def move_to_x(self, desired_x):
        """
        Set a new target position and direction.

        Args:
            desired_x (float): Desired target position.
        """
        self.target_x = desired_x
        if self.current_x < desired_x:
            self.direction = Direction.POSITIVE
        elif self.current_x > desired_x:
            self.direction = Direction.NEGATIVE
        else:
            self.direction = Direction.STATIONARY

    def get_x(self):
        """
        Get the current position.
        """
        return self.current_x

    def get_velocity(self):
        """
        Get the current velocity.
        """
        return self.velocity


class Direction(enum.Enum):
    STATIONARY = 0
    POSITIVE = 1
    NEGATIVE = -1