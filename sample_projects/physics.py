"""
Simple 2D physics engine.
"""

import math


GRAVITY = 9.81
TIME_STEP = 0.016


class PhysicsEngine:
    """Handles simple physics updates."""

    def __init__(self, gravity=GRAVITY):
        self.gravity = gravity

    def apply_gravity(self, body):
        """Adds gravity to a body's vertical velocity."""
        body.velocity_y += self.gravity * TIME_STEP

    def update_position(self, body):
        """Moves a body according to its velocity."""
        body.x += body.velocity_x * TIME_STEP
        body.y += body.velocity_y * TIME_STEP

    def simulate(self, bodies):
        """Runs one frame of the simulation."""
        for body in bodies:
            self.apply_gravity(body)
            self.update_position(body)


class RigidBody:
    """Represents a simple object in the world."""

    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

        self.velocity_x = 0
        self.velocity_y = 0

    def apply_force(self, fx, fy):
        """Changes velocity based on a force."""
        self.velocity_x += fx / self.mass
        self.velocity_y += fy / self.mass


def distance(body1, body2):
    """Returns the distance between two bodies."""
    dx = body2.x - body1.x
    dy = body2.y - body1.y

    return math.sqrt(dx ** 2 + dy ** 2)


def detect_collision(body1, body2, radius):
    """Checks if two circular bodies overlap."""
    return distance(body1, body2) <= radius * 2


def clamp(value, minimum, maximum):
    """Restricts a value to a given range."""
    return max(minimum, min(value, maximum))