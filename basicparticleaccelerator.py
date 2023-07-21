import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PARTICLE_RADIUS = 5
MAGNET_STRENGTH = 0.1
MAGNET_WIDTH, MAGNET_HEIGHT = 100, 30
MAGNET_COUNT = 6

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Particle Accelerator Simulation')

# Particle class
class Particle:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity

    def move(self):
        self.x += self.velocity

# Magnet class
class Magnet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, MAGNET_WIDTH, MAGNET_HEIGHT))

# Function to calculate the bending force on the particle due to the magnets
def calculate_force(particle, magnet):
    distance = math.sqrt((particle.x - magnet.x) ** 2 + (particle.y - magnet.y) ** 2)
    return MAGNET_STRENGTH / distance ** 2

# Function to update the particle's velocity due to the magnets
def update_velocity(particle, magnets):
    for magnet in magnets:
        force = calculate_force(particle, magnet)
        particle.velocity += force

# Main function
def main():
    # Create the particle and magnets
    particle = Particle(50, SCREEN_HEIGHT // 2, 3)
    magnets = [Magnet(200 + i * 150, SCREEN_HEIGHT // 2 - MAGNET_HEIGHT // 2) for i in range(MAGNET_COUNT)]

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(WHITE)

        # Update the particle's velocity
        update_velocity(particle, magnets)

        # Move the particle
        particle.move()

        # Draw the particle
        pygame.draw.circle(screen, BLACK, (int(particle.x), int(particle.y)), PARTICLE_RADIUS)

        # Draw the magnets
        for magnet in magnets:
            magnet.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
