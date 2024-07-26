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
            noise_value = noise.pnoise3(i / scale, j / scale + time, time / 2,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=width,
                                        repeaty=height,
                                        base=42)
            noise_array[i][j] = noise_value
    return noise_array


def qsub8(a, b):
    """Subtract b from a, but not less than 0."""
    return max(a - b, 0)


def abs8(x):
    """Absolute value for 8-bit number."""
    return abs(x)


def map_to_palette(value, palette, j, num_rows):
    # Перевод значений от -1 до 1 в диапазон от 0 до 255
    index = int((value + 1) * 128)
    index = qsub8(index, abs8(j - (num_rows - 1)) * 255 // (num_rows + 2))
    index = min(max(index, 0), 255)
    color_index = int(index * (len(palette) - 1) / 255)

    # color_index = int((value + 1) / 2 * (len(palette) - 1))  # Перевод значений от -1 до 1 в индексы палитры
    return palette[color_index]


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
            color = map_to_palette(noise_array[x][y], palette, y, HEIGHT)
            pygame.draw.rect(screen, color, (x * scale_xy, y * scale_xy, scale_xy, scale_xy))

    pygame.display.flip()
    clock.tick(30)  # Ограничение FPS до 30

    time += 0.1  # Увеличиваем время для анимации шума

pygame.quit()
