import pygame
import numpy as np
import random
import math

scale_xy = 30

# Параметры подключения
x_size = 16 * 2
y_size = 16 * 2

# Параметры алгоритма
fire_dT = 10  # задержка обработки модели огня в мс
fire_loss = 0.95  # коэффициент потери энергии
fire_smooth = 0.5  # Коэффициент сглаженности распределения энергии частиц
sig = y_size  # ширина пламени
dlt = 180  # общая мощность пламени
mlt = 5 * 600  # усиление возгорания
Hue = 0  # Цвет пламени (0- красный)
H0 = 0
H255 = 60
S0 = 200
S255 = 255
V0 = 0
V255 = 255

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((x_size * scale_xy, y_size * scale_xy))
pygame.display.set_caption("Fire Simulation")

# Картина возгорания
fire_frame = np.zeros((y_size, x_size), dtype=np.uint8)
# Распределение вероятностей возгорания
fire_prob = np.zeros(x_size, dtype=np.uint8)


def generate_prob(sigma, mult):
    for i in range(x_size):
        fire_prob[i] = round(mult * (1 / (sigma * 2.5)) * math.exp(-((i - (x_size / 2)) ** 2) / (2 * (sigma ** 2))))


def hsv_to_rgb(h, s, v):
    if s == 0:
        return v, v, v
    h = float(h) / 256 * 6
    i = int(h)
    f = h - i
    p = v * (1 - s / 255)
    q = v * (1 - s / 255 * f)
    t = v * (1 - s / 255 * (1 - f))
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q


def e_to_color(e):
    h = Hue + np.interp(e, [0, 255], [H0, H255])
    s = np.clip(np.interp(e, [0, 255], [S255, S0]), 0, 255)
    v = np.clip(np.interp(e, [0, 255], [V0, V255]), 0, 255)
    r, g, b = hsv_to_rgb(h, s, v)
    return (int(r), int(g), int(b))


def update_fire():
    global fire_frame
    # Сдвиг матрицы
    fire_frame[1:] = fire_frame[:-1] * fire_loss
    # Заполнение нижней строки псевдослучайными числами
    for x in range(x_size):
        fire_old = fire_frame[0][x]
        #fire_frame[0][x] = round(fire_old + (random.randint(fire_prob[x], fire_prob[x] + dlt) - fire_old) * fire_smooth)
        new_value = fire_old + (random.randint(fire_prob[x], fire_prob[x] + dlt) - fire_old) * fire_smooth
        fire_frame[0][x] = np.clip(round(new_value), 0, 255)


def draw_fire():
    screen.fill((0, 0, 0))
    for y in range(y_size):
        for x in range(x_size):
            color = e_to_color(fire_frame[y][x])
            pygame.draw.rect(screen, color, (x * scale_xy, (y_size - y - 1) * scale_xy, scale_xy, scale_xy))
    pygame.display.update()


# Основная программа
generate_prob(sig, mlt)

clock = pygame.time.Clock()
running = True
old_T = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_T = pygame.time.get_ticks()
    if current_T - old_T > fire_dT:
        old_T = current_T
        update_fire()
        draw_fire()

    clock.tick(30)

pygame.quit()
