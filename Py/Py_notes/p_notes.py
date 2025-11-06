import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("My Pygame Window")

# Circle position stored separately
corcle_x, corcle_y = 600, 360
radius = 50

while True:
    screen.fill((255, 0, 255))

    # Draw shapes
    pygame.draw.circle(screen, (0, 255, 0), (corcle_x, corcle_y), radius)
    pygame.draw.rect(screen, (0, 0, 255), (500, 100, 200, 120))
    pygame.draw.polygon(screen, (255, 255, 0), [(600, 500), (700, 650), (500, 650)])

    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Handle key presses (continuous)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        corcle_x -= 5
    if keys[pygame.K_RIGHT]:
        corcle_x += 5
    if keys[pygame.K_UP]:
        corcle_y -= 5
    if keys[pygame.K_DOWN]:
        corcle_y += 5

    pygame.display.flip()
