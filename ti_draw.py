# JuliNator99 - juli.schwers@gmail.com
import pygame
import math

# Start of INIT
pygame.init()  # Initialize pygame
__color = (0, 0, 0)  # Assign default pen color
__screen = pygame.display.set_mode((1920, 1080))  # Create display
__automatic_updates = True


# INTERNAL FUNCTIONS
def __pixel(x, y):
  __screen.set_at((x, y), __color)


# TI CONTROL
def clear():
  __screen.fill("white")

  if __automatic_updates:
    paint_buffer()


def clear_rect(x, y, width, height):
  __screen.fill("white", (x, y, width, height))

  if __automatic_updates:
    paint_buffer()


def set_color(red, green, blue):
  global __color
  __color = (red, green, blue)


def get_screen_dim():
  return __screen.get_width(), __screen.get_height()


def use_buffer():
  global __automatic_updates
  __automatic_updates = False


def paint_buffer():
  pygame.display.flip()


# TI Form
def fill_rect(x, y, width, height):
  for posX in range(0, width):
    for posY in range(0, height):
      __pixel(posX + x, posY + y)

  if __automatic_updates:
    paint_buffer()


def draw_rect(x, y, height, width):
  for i in range(2):
    for posX in range(width + 1):
      __pixel(x + posX, y + i * height)
    for posY in range(height + 1):
      __pixel(x + i * width, y + posY)

  if __automatic_updates:
    paint_buffer()


def fill_circle(x, y, radius):
  for posX in range(2 * radius + 1):
    for posY in range(2 * radius + 1):
      xx = x + radius - posX
      yy = y + radius - posY
      if int(math.sqrt((x - xx) ** 2 + (y - yy) ** 2)) <= radius:
        __pixel(xx, yy)

  if __automatic_updates:
    paint_buffer()


def draw_circle(x, y, radius):
  for posX in range(2 * radius + 1):
    for posY in range(2 * radius + 1):
      xx = x + radius - posX
      yy = y + radius - posY
      if int(math.sqrt((x - xx) ** 2 + (y - yy) ** 2)) == radius:
        __pixel(xx, yy)

  if __automatic_updates:
    paint_buffer()


def draw_line(x1, y1, x2, y2):
  dx, dy = abs(x2 - x1), abs(y2 - y1)
  step_x = 1 if x1 < x2 else -1
  step_y = 1 if y1 < y2 else -1
  error = dx - dy

  while (x1, y1) != (x2, y2):
    __pixel(x1, y1)
    if error * 2 > -dy:
      error -= dy
      x1 += step_x
    if error * 2 < dx:
      error += dx
      y1 += step_y

  __pixel(x2, y2)
  if __automatic_updates:
    paint_buffer()


# Continue of INIT
clear()  # Clear screen