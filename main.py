# JuliNator99 - juli.schwers@gmail.com
import random
from math import floor

from Object import Sphere
from Renderer import *
from Scene import Scene, Point
from ti_draw import *
from ti_system import *

quality = 10
reflections = 0
width = floor(get_screen_dim()[0] / quality)
height = floor(get_screen_dim()[1] / quality)
scene = Scene([Sphere(Material((235 / 255, 52 / 255, 113 / 255)), Point(0.0, 5.0, 0.0), 0.8),
               Sphere(Material((200 / 255, 255 / 255, 10 / 255)), Point(3.0, 5.0, 0.0), 1.0),
               Sphere(Material((10 / 255, 255 / 255, 104 / 255)), Point(-3.0, 5.0, 0.0), 1.0),
               Sphere(Material((10 / 255, 226 / 255, 255 / 255)), Point(-1.5, 6.0, 2.0), 1.0),
               Sphere(Material((10 / 255, 63 / 255, 255 / 255)), Point(1.5, 6.0, -2.0), 1.0),
               Sphere(Material((182 / 255, 64 / 255, 255 / 255)), Point(0, -20.0, -0.0), 15.0)],
              [Point(0.0, 5.0, 5.0)])
camera = Camera(Point(0.0, -2.0, 0.0),
                Point(0.0, 1.0, 0.0),
                70.0,
                width / height,
                Point(0.0, 0.0, 1.0))
renderer = DefaultRenderer(camera, scene)
cancelled = False

use_buffer()

iterations = 0
while not cancelled:
  positions = [v for v in (range(0, width * height))]
  random.shuffle(positions)

  for position in positions:
    x = position % width
    y = floor(position / width)
    material = renderer.render((x / float(width), y / float(height)), reflections)

    color = int(material.color[0] * 255), int(material.color[1] * 255), int(material.color[2] * 255)
    set_color(color[0], color[1], color[2])
    fill_rect(x * quality, y * quality, quality, quality)

    key = get_key()
    if camera.process_movement(key): break
    if key == "esc":
      cancelled = True
      break
    if key == "q":
      quality = 1
      reflections = 3
      width = floor(get_screen_dim()[0] / quality)
      height = floor(get_screen_dim()[1] / quality)
      break
    if iterations == 1000:
      paint_buffer()
      iterations = 0

    iterations += 1

  paint_buffer()