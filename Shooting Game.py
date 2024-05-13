import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player
player_size = 50
player = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT - 2 * player_size, player_size, player_size)
player_speed = 5

# Enemies
enemy_size = 50
enemy_speed = 3
enemies = []
enemy_spawn_time = 30
enemy_spawn_counter = 0

# Bullets
bullet_size = 10
bullet_speed = 5
bullets = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx - bullet_size // 2, player.top, bullet_size, bullet_size))
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    
    # Enemy spawning
    enemy_spawn_counter += 1
    if enemy_spawn_counter == enemy_spawn_time:
        enemy_spawn_counter = 0
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemies.append(pygame.Rect(enemy_x, 0, enemy_size, enemy_size))
    
    # Update and draw enemies
    for enemy in enemies:
        enemy.y += enemy_speed
        pygame.draw.rect(screen, RED, enemy)
        if enemy.y >= HEIGHT:
            enemies.remove(enemy)
            score += 1
    
    # Update and draw bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        pygame.draw.rect(screen, BLUE, bullet)
        if bullet.y < 0:
            bullets.remove(bullet)
    
    # Collision detection
    for enemy in enemies:
        for bullet in bullets:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10
    
    # Draw player
    pygame.draw.rect(screen, BLUE, player)
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
