import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Fonts
SCORE_FONT = pygame.font.SysFont("comicsans", 50)

def draw(win, paddles, ball, scores):
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, paddles[0])
    pygame.draw.rect(win, WHITE, paddles[1])
    pygame.draw.ellipse(win, WHITE, ball)
    pygame.draw.aaline(win, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    score_text = SCORE_FONT.render(f"{scores[0]}   {scores[1]}", 1, WHITE)
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    pygame.display.update()

def main():
    # Paddles: [left, right]
    left_paddle = pygame.Rect(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH-20, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddles = [left_paddle, right_paddle]

    # Ball
    ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
    ball_vel = [BALL_SPEED_X, BALL_SPEED_Y]

    # Scores
    scores = [0, 0]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Player input
        keys = pygame.key.get_pressed()
        # Left paddle (W/S)
        if keys[pygame.K_w] and paddles[0].top > 0:
            paddles[0].y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddles[0].bottom < HEIGHT:
            paddles[0].y += PADDLE_SPEED
        # Right paddle (Up/Down)
        if keys[pygame.K_UP] and paddles[1].top > 0:
            paddles[1].y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddles[1].bottom < HEIGHT:
            paddles[1].y += PADDLE_SPEED

        # Ball movement
        ball.x += ball_vel[0]
        ball.y += ball_vel[1]

        # Ball collision with top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_vel[1] *= -1

        # Ball collision with paddles
        if ball.colliderect(paddles[0]) and ball_vel[0] < 0:
            ball_vel[0] *= -1
        if ball.colliderect(paddles[1]) and ball_vel[0] > 0:
            ball_vel[0] *= -1

        # Ball out of bounds (score)
        if ball.left <= 0:
            scores[1] += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_vel = [BALL_SPEED_X, BALL_SPEED_Y]
        if ball.right >= WIDTH:
            scores[0] += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_vel = [-BALL_SPEED_X, BALL_SPEED_Y]

        draw(WIN, paddles, ball, scores)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()