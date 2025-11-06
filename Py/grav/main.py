import pygame, math
pygame.init()

# --- Setup ---
screen = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Physics + Collision Demo")
clock = pygame.time.Clock()

GRAVITY = 0.5
BOUNCE = 0.7  # energy loss on bounce
FRICTION = 0.98

# --- Class Definition ---
class GameObject:
    def __init__(self, x, y, color, shape="circle", size=50):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.color = color
        self.shape = shape
        self.size = size
        self.on_ground = False

    def apply_gravity(self):
        if not self.on_ground:
            self.vy += GRAVITY

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off screen edges
        if self.x - self.size < 0:
            self.x = self.size
            self.vx *= -BOUNCE
        elif self.x + self.size > 1200:
            self.x = 1200 - self.size
            self.vx *= -BOUNCE

        # Bounce off ground
        if self.y + self.size > 720:
            self.y = 720 - self.size
            self.vy *= -BOUNCE
            self.vx *= FRICTION
            if abs(self.vy) < 1:
                self.vy = 0
                self.on_ground = True
        else:
            self.on_ground = False

    def draw(self, screen):
        if self.shape == "circle":
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        elif self.shape == "rect":
            pygame.draw.rect(screen, self.color, (self.x - self.size, self.y - self.size, self.size*2, self.size*2))
        elif self.shape == "triangle":
            pygame.draw.polygon(screen, self.color, [
                (self.x, self.y - self.size),
                (self.x + self.size, self.y + self.size),
                (self.x - self.size, self.y + self.size)
            ])

# --- Collision Handling (circle-based for simplicity) ---
def handle_collisions(objects):
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            obj1 = objects[i]
            obj2 = objects[j]

            # Distance between centers
            dx = obj2.x - obj1.x
            dy = obj2.y - obj1.y
            dist = math.hypot(dx, dy)
            min_dist = obj1.size + obj2.size

            if dist < min_dist and dist != 0:
                # Overlap amount
                overlap = 0.5 * (min_dist - dist + 1)

                # Normalize direction
                nx = dx / dist
                ny = dy / dist

                # Separate them
                obj1.x -= overlap * nx
                obj1.y -= overlap * ny
                obj2.x += overlap * nx
                obj2.y += overlap * ny

                # Swap velocities (elastic collision)
                obj1.vx, obj2.vx = obj2.vx * BOUNCE, obj1.vx * BOUNCE
                obj1.vy, obj2.vy = obj2.vy * BOUNCE, obj1.vy * BOUNCE

# --- Create objects ---
circle = GameObject(600, 100, (0, 255, 0), "circle", 50)
rect = GameObject(500, 50, (0, 0, 255), "rect", 40)

objects = [circle, rect]

# --- Main Loop ---
running = True
while running:
    dt = clock.tick(60)
    screen.fill((255, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle.vx -= 0.5
    if keys[pygame.K_RIGHT]:
        circle.vx += 0.5
    if keys[pygame.K_UP] and circle.on_ground:
        circle.vy = -12

    # Physics
    for obj in objects:
        obj.apply_gravity()
        obj.move()

    handle_collisions(objects)

    # Draw
    for obj in objects:
        obj.draw(screen)

    pygame.display.flip()

pygame.quit()
