# JuliNator99 - juli.schwers@gmail.com
import math

from Material import Material


class Point:
  def __init__(self, x: float, y: float, z: float):
    self.x = x
    self.y = y
    self.z = z

  # Operations
  def plus(self, point):
    return Point(self.x + point.x, self.y + point.y, self.z + point.z)

  def plusv(self, value):
    return Point(self.x + value, self.y + value, self.z + value)

  def minus(self, point):
    return Point(self.x - point.x, self.y - point.y, self.z - point.z)

  def minusv(self, value):
    return Point(self.x - value, self.y - value, self.z - value)

  def times(self, point):
    return Point(self.x * point.x, self.y * point.y, self.z * point.z)

  def timesv(self, value):
    return Point(self.x * value, self.y * value, self.z * value)

  def div(self, point):
    return Point(self.x / point.x, self.y / point.y, self.z / point.z)

  def divv(self, value):
    return Point(self.x / value, self.y / value, self.z / value)

  def distance_to(self, point):
    difference = self.minus(point)
    return difference.length()

  def dot(self, point):
    return self.x * point.x + self.y * point.y + self.z * point.z

  def cross(self, point):
    return Point(self.y * point.z - self.z * point.y, self.z * point.x - self.x * point.z, self.x * point.y - self.y * point.x)

  def length(self):
    return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

  def normalized(self):
    length = self.length()
    return Point(self.x / length, self.y / length, self.z / length)

  def reversed(self):
    return self.timesv(-1)

  def reflect_using(self, normal):
    return self.minus(normal.timesv(2.0 * self.dot(normal)))


class Ray:
  def __init__(self, point: Point, direction: Point):
    self.point = point
    self.direction = direction.normalized()

  def interpolate(self, value):
    direction = self.direction.timesv(value)
    return self.point.plus(direction)


class Intersection:
  def __init__(self, material: Material, point: Point, intersection_normal: Point, from_ray: Ray, iterations: int):
    self.material = material
    self.point = point
    self.from_ray = from_ray
    self.intersection_normal = intersection_normal
    self.iterations = iterations


class Scene:
  def __init__(self, objects, lights):
    self.objects = objects
    self.lights = lights

  def nearest_distance(self, position: (float, float, float)):
    nearest = None
    nearest_object = None

    for part in self.objects:
      distance = part.get_distance(position)

      if nearest is None or distance < nearest:
        nearest = distance
        nearest_object = part

    return nearest_object, nearest