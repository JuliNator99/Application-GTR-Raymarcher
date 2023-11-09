# JuliNator99 - juli.schwers@gmail.com
import math
from Scene import Point, Ray


class Camera:
  def __init__(self, position: Point, direction: Point, fov: float, aspect_ratio: float, up: Point):
    self.__position = position
    self.__direction = direction.normalized()
    self.__fov = fov
    self.__aspect_ratio = aspect_ratio
    self.__up = up
    self.__right = self.__up.cross(self.__direction).normalized()
    self.__up_adjusted = self.__direction.cross(self.__right).normalized()
    self.__fov_radians = math.radians(fov)
    self.__half_height = math.tan(self.__fov_radians / 2.0)
    self.__half_width = self.__aspect_ratio * self.__half_height

  def get_ray(self, pixel: (float, float)):
    normalised_x = (pixel[0] - 0.5) * self.__aspect_ratio
    normalised_y = (pixel[1] - 0.5) * self.__aspect_ratio

    direction = self.__get_direction((normalised_x, normalised_y))
    return Ray(self.__position, direction)

  def __get_direction(self, normalised: (float, float)):
    right = self.__right.timesv(normalised[0]).timesv(self.__half_width)
    up = self.__up_adjusted.timesv(normalised[1]).timesv(self.__half_height)

    return self.__direction.plus(right).plus(up)

  def process_movement(self, key):
    match key:
      case "8":
        self.move_forward(0.5)
        return True
      case "2":
        self.move_forward(-0.5)
        return True
      case "6":
        self.move_right(0.5)
        return True
      case "4":
        self.move_right(-0.5)
        return True
    return False

  def move_forward(self, value):
    self.__position = self.__position.plus(self.__direction.timesv(value))

  def move_right(self, value):
    self.__position = self.__position.plus(self.__right.timesv(value))