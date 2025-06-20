import pygame
import random
import time

pygame.init()

# Экран с иконкой и названием игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

# Цель
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Звук попадания
hit_sound = pygame.mixer.Sound("img/zvuk.wav")

# Шрифт и очки
font = pygame.font.SysFont("Arial", 36)
score = 0

# Таймер
game_duration = 30  # секунд
start_time = time.time()

# Игровой цикл
running = True
game_over = False

while running:
    current_time = time.time()
    elapsed_time = int(current_time - start_time)
    time_left = max(0, game_duration - elapsed_time)

    if time_left == 0:
        game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (target_x < mouse_x < target_x + target_width and
                target_y < mouse_y < target_y + target_height):
                score += 1
                hit_sound.play()
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill(color)

    if not game_over:
        screen.blit(target_img, (target_x, target_y))

    # Отображение очков и таймера
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    time_text = font.render(f"Время: {time_left}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    # Если игра окончена — выводим финальный текст
    if game_over:
        game_over_text = font.render("Игра окончена!", True, (255, 0, 0))
        final_score_text = font.render(f"Твой счёт: {score}", True, (255, 255, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 40))
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 10))

    pygame.display.update()

pygame.quit()
