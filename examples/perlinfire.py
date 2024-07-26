import pygame
import noise
import numpy as np

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 64, 64
scale_xy = 3
screen_width, screen_height = WIDTH * scale_xy, HEIGHT * scale_xy
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Perlin Noise Fire')

# Параметры Perlin noise
scale = 10.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

# Цветовая палитра огня (пример)
palette = [
    (0, 0, 0),
    (32, 0, 0),
    (64, 0, 0),
    (128, 0, 0),
    (255, 0, 0),
    (255, 64, 0),
    (255, 128, 0),
    (255, 255, 0),
    (255, 255, 128),
    (255, 255, 255),
]


def generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity, time):
    noise_array = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            noise_value = noise.pnoise3(i / scale, j / scale, time,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=width,
                                        repeaty=height,
                                        base=42)
            noise_array[i][j] = noise_value


    return noise_array


def map_to_palette(value, palette):
    index = int((value + 1) / 2 * (len(palette) - 1))  # Перевод значений от -1 до 1 в индексы палитры
    return palette[index]


# Основной цикл
running = True
time = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Генерация шума с учетом времени
    noise_array = generate_perlin_noise(WIDTH, HEIGHT, scale, octaves, persistence, lacunarity, time)

    # Отрисовка огня
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = map_to_palette(noise_array[x][y], palette)
            pygame.draw.rect(screen, color, (x * scale_xy, y * scale_xy, scale_xy, scale_xy))

    pygame.display.flip()
    clock.tick(30)  # Ограничение FPS до 30

    time += 0.1  # Увеличиваем время для анимации шума

pygame.quit()
