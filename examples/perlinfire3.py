import pygame
import noise
import numpy as np

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 64, 64
# scale_xy = 7

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
scale_xy = min(screen_width // WIDTH, screen_height // HEIGHT) - 1  # Оставляем 1 пиксель для отступа

screen_width, screen_height = WIDTH * scale_xy, HEIGHT * scale_xy
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Perlin Noise Fire')

# Параметры Perlin noise
scale = 10.0  # Этот масштаб делает шум более крупнозернистым. Если уменьшить значение, узоры станут более плотными
octaves = 6  # Шум будет состоять из 6 слоев с разной частотой и амплитудой, что добавляет больше детализации
persistence = 0.5  # Амплитуда каждой октавы уменьшается в 2 раза (50%) по сравнению с предыдущей. Это создаёт баланс между детализацией и плавностью
lacunarity = 2.0  # Частота каждой октавы удваивается. Это стандартное значение для создания фрактальных узоров

# Градиентная палитра
firepal = [
    (0, 0, 0, 0),  # black at position 0
    (32, 255, 0, 0),  # red at position 32
    (190, 255, 255, 0),
    (255, 255, 0, 0)
]

# Цветовая палитра огня (пример)
# palette = [
#     (0, 0, 0),
#     (32, 0, 0),
#     (64, 0, 0),
#     (128, 0, 0),
#     (255, 0, 0),
#     (255, 64, 0),
#     (255, 128, 0),
#     (255, 255, 0),
#     (255, 255, 128),
#     (255, 255, 255),
# ]


def interpolate_color(c1, c2, t):
    """Interpolate between two colors."""
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def get_gradient_color(palette, value):
    """Get color from gradient palette."""
    value = int(value * 255)
    for i in range(len(palette) - 1):
        if palette[i][0] <= value <= palette[i + 1][0]:
            t = (value - palette[i][0]) / (palette[i + 1][0] - palette[i][0])
            return interpolate_color(palette[i][1:], palette[i + 1][1:], t)
    return palette[-1][1:]


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


def map_to_palette(value, palette, j, num_rows, fire_strength):
    # Перевод значений от -1 до 1 в диапазон от 0 до 255
    index = int((value + 1) * 128)
    index = qsub8(index, abs8(j - (num_rows - 1)) * 255 // (num_rows + 2))
    index = int(index * fire_strength)
    index = min(max(index, 0), 255)
    # color_index = int(index * (len(palette) - 1) / 255)
    # return palette[color_index]

    return get_gradient_color(palette, index / 255)


# Начальные параметры огня
fire_strength = 1.0
fire_height_offset = 0
block_spacing = 1  # Начальное значение отступа между блоками

# Основной цикл
running = True
time = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Управление параметрами огня
            if event.key == pygame.K_UP:
                fire_strength = min(fire_strength + 0.1, 2.0)
            elif event.key == pygame.K_DOWN:
                fire_strength = max(fire_strength - 0.1, 0.0)
            # elif event.key == pygame.K_w:
            #     fire_height_offset = max(fire_height_offset - 1, -HEIGHT // 2)
            # elif event.key == pygame.K_s:
            #     fire_height_offset = min(fire_height_offset + 1, HEIGHT // 2)
            # elif event.key == pygame.K_SPACE:
            #     fire_strength = 0.0  # Затушить огонь

            # Управление параметрами Perlin noise
            # Верхний ряд - увеличение
            elif event.key == pygame.K_q:
                scale += 0.5
            elif event.key == pygame.K_w:
                octaves += 1
            elif event.key == pygame.K_e:
                persistence = min(persistence + 0.05, 1.0)
            elif event.key == pygame.K_r:
                lacunarity = min(lacunarity + 0.1, 5.0)

            # Средний ряд - сброс
            elif event.key == pygame.K_a:
                scale = 10.0
            elif event.key == pygame.K_s:
                octaves = 6
            elif event.key == pygame.K_d:
                persistence = 0.5
            elif event.key == pygame.K_f:
                lacunarity = 2.0

            # Нижний ряд - уменьшение
            elif event.key == pygame.K_z:
                scale = max(scale - 0.5, 1.0)
            elif event.key == pygame.K_x:
                octaves = max(octaves - 1, 1)
            elif event.key == pygame.K_c:
                persistence = max(persistence - 0.05, 0.0)
            elif event.key == pygame.K_v:
                lacunarity = max(lacunarity - 0.1, 1.0)

            # Управление отступами между блоками
            elif event.key == pygame.K_t:
                block_spacing += 1  # Увеличение отступа
                screen.fill((0, 0, 0))
                scale_xy = min(screen_width // WIDTH, screen_height // HEIGHT) - block_spacing
            elif event.key == pygame.K_g:
                block_spacing = 1  # Сброс отступа к 1
                screen.fill((0, 0, 0))
                scale_xy = min(screen_width // WIDTH, screen_height // HEIGHT) - block_spacing
            elif event.key == pygame.K_b:
                block_spacing = max(block_spacing - 1, 0)  # Уменьшение отступа, но не меньше 0
                screen.fill((0, 0, 0))
                scale_xy = min(screen_width // WIDTH, screen_height // HEIGHT) - block_spacing

    # Генерация шума с учетом времени
    noise_array = generate_perlin_noise(WIDTH, HEIGHT, scale, octaves, persistence, lacunarity, time)

    # Отрисовка огня
    for y in range(HEIGHT):
        for x in range(WIDTH):
            adjusted_y = y + fire_height_offset
            if 0 <= adjusted_y < HEIGHT:
                color = map_to_palette(noise_array[x][adjusted_y], firepal, y, HEIGHT, fire_strength)
                # pygame.draw.rect(screen, color, (x * scale_xy, y * scale_xy, scale_xy, scale_xy))
                pygame.draw.rect(screen, color, (x * (scale_xy + block_spacing), y * (scale_xy + block_spacing), scale_xy, scale_xy))
            else:
                # pygame.draw.rect(screen, (0, 0, 0),
                #                  (x * scale_xy, y * scale_xy, scale_xy, scale_xy))  # Черный цвет за пределами огня
                pygame.draw.rect(screen, (0, 0, 0), (
                x * (scale_xy + 1), y * (scale_xy + 1), scale_xy, scale_xy))  # Черный цвет за пределами огня

    pygame.display.flip()
    clock.tick(30)  # Ограничение FPS до 30

    time += 0.1  # Увеличиваем время для анимации шума

pygame.quit()
