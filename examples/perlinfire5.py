import pygame
import noise
import numpy as np

# Инициализация Pygame
from numpy.random import random

pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 16, 16
# WIDTH, HEIGHT = 64, 64
# scale_xy = 7

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
scale_xy = min(screen_width // WIDTH, screen_height // HEIGHT) - 1  # Оставляем 1 пиксель для отступа

screen_width, screen_height = WIDTH * scale_xy, HEIGHT * scale_xy
# screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Perlin Noise Fire')

# Параметры Perlin noise
scale = 5#10.0  # Этот масштаб делает шум более крупнозернистым. Если уменьшить значение, узоры станут более плотными
octaves = 2#6  # Шум будет состоять из 6 слоев с разной частотой и амплитудой, что добавляет больше детализации
persistence = 0.25#0.5  # Амплитуда каждой октавы уменьшается в 2 раза (50%) по сравнению с предыдущей. Это создаёт баланс между детализацией и плавностью
lacunarity = 3#2.0  # Частота каждой октавы удваивается. Это стандартное значение для создания фрактальных узоров

# Градиентная палитра
firepal = [
    (0, 0, 0, 0),  # black at position 0
    (16, 255, 0, 0),  # red at position 32
    (220, 255, 255, 0),
    (255, 255, 255, 255)
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
fire_intensity = 0.0  # Изначально огонь не горит
block_spacing = 2#1  # Начальное значение отступа между блоками

oxy = 1.3#1.5

# Создаем массив для хранения энергии огня для каждой строки
fire_energy = np.zeros(HEIGHT)

# Основной цикл
running = True
time = 0
clock = pygame.time.Clock()

# Шрифт для отображения текста
font = pygame.font.SysFont(None, 24)

while running:
    if fire_intensity > 0:
        fire_intensity -= 0.05
    if random() > 0.85:
        fire_intensity += random() / 2
        if fire_intensity > 1:
            fire_intensity = 1
    fire_intensity = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Нажатие клавиши ENTER
                fire_intensity = 1
            # Управление параметрами Perlin noise
            elif event.key == pygame.K_q:
                scale += 0.5
            elif event.key == pygame.K_w:
                octaves += 1
            elif event.key == pygame.K_e:
                persistence = min(persistence + 0.05, 1.0)
            elif event.key == pygame.K_r:
                lacunarity = min(lacunarity + 0.1, 5.0)
            elif event.key == pygame.K_a:
                scale = 10.0
            elif event.key == pygame.K_s:
                octaves = 6
            elif event.key == pygame.K_d:
                persistence = 0.5
            elif event.key == pygame.K_f:
                lacunarity = 2.0
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
                # screen.fill((0, 0, 0))
                scale_xy = min(screen_width // WIDTH, screen_height // HEIGHT) - block_spacing
            elif event.key == pygame.K_g:
                block_spacing = 1  # Сброс отступа к 1
                # screen.fill((0, 0, 0))
                scale_xy = min(screen_width // WIDTH, screen_height // HEIGHT) - block_spacing
            elif event.key == pygame.K_b:
                block_spacing = max(block_spacing - 1, 0)  # Уменьшение отступа, но не меньше 0
                # screen.fill((0, 0, 0))
                scale_xy = min(screen_width // WIDTH, screen_height // HEIGHT) - block_spacing

            # Управление кислородом
            elif event.key == pygame.K_y:
                oxy += 0.1  # Увеличение
            elif event.key == pygame.K_h:
                oxy = 1  # Сброс к 1
            elif event.key == pygame.K_n:
                oxy = max(oxy - 0.1, 0)  # Уменьшение, но не меньше 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:  # Отпускание клавиши ENTER
                fire_intensity = 0.0
                # print(fire_intensity)

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Генерация шума с учетом времени
    noise_array = generate_perlin_noise(WIDTH, HEIGHT, scale, octaves, persistence, lacunarity, time)

    # Обновление энергии огня
    fire_energy[-1] = fire_intensity  # Обновление нижней строки
    for y in range(HEIGHT - 2, -1, -1):
        stop_perc = 0.25 # старая энергия
        start_perc = 1 - stop_perc  # соседняя энергия
        stop_perc *= oxy
        # start_perc *= oxy
        fire_energy[y] = max(fire_energy[y] * stop_perc, 0.0) + \
                         max(fire_energy[y + 1] * start_perc, 0.0)  # Перемещение энергии вверх

    # Отрисовка огня
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = map_to_palette(noise_array[x][y], firepal, y, HEIGHT, fire_energy[y])
            pygame.draw.rect(screen, color,
                             (x * (scale_xy + block_spacing), y * (scale_xy + block_spacing), scale_xy, scale_xy))

    # Вывод параметров на экран
    param_text = f"Scale: {scale:.1f}, Octaves: {octaves}, Persistence: {persistence:.2f}, Lacunarity: {lacunarity:.2f}, Block Spacing: {block_spacing}, oxy: {oxy}"
    text_surface = font.render(param_text, True, (255, 255, 255))
    screen.blit(text_surface, ((WIDTH + 1) * scale_xy, 10))

    pygame.display.flip()
    clock.tick(30)  # Ограничение FPS до 30

    time += 0.1  # Увеличиваем время для анимации шума

pygame.quit()
