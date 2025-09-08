
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game objects
player_paddle = pygame.Rect(50, HEIGHT // 2 - 50, 10, 100)
opponent_paddle = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 50, 10, 100)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

# Game variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH / 2, HEIGHT / 2)
    ball_speed_y *= -1
    ball_speed_x *= -1

def main():
    global player_speed, ball_speed_x, ball_speed_y, player_score, opponent_score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed -= 7
                if event.key == pygame.K_DOWN:
                    player_speed += 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_speed += 7
                if event.key == pygame.K_DOWN:
                    player_speed -= 7

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1
        if ball.left <= 0:
            opponent_score += 1
            ball_restart()
        if ball.right >= WIDTH:
            player_score += 1
            ball_restart()

        if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
            ball_speed_x *= -1

        # Player movement
        player_paddle.y += player_speed
        if player_paddle.top <= 0:
            player_paddle.top = 0
        if player_paddle.bottom >= HEIGHT:
            player_paddle.bottom = HEIGHT

        # Opponent AI
        if opponent_paddle.top < ball.y:
            opponent_paddle.top += opponent_speed
        if opponent_paddle.bottom > ball.y:
            opponent_paddle.bottom -= opponent_speed
        if opponent_paddle.top <= 0:
            opponent_paddle.top = 0
        if opponent_paddle.bottom >= HEIGHT:
            opponent_paddle.bottom = HEIGHT

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player_paddle)
        pygame.draw.rect(screen, WHITE, opponent_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

        player_text = font.render(f"{player_score}", True, WHITE)
        screen.blit(player_text, (WIDTH / 2 - 50, 50))

        opponent_text = font.render(f"{opponent_score}", True, WHITE)
        screen.blit(opponent_text, (WIDTH / 2 + 25, 50))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
