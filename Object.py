# JuliNator99 - juli.schwers@gmail.com
from Material import Material
from Scene import Point


class Object:
  def get_distance(self, point): pass

  def get_normal(self, point): pass


class Sphere(Object):
  def __init__(self, material: Material, point: Point, radius: float):
    self.material = material
    self.point = point
    self.radius = radius

  def get_distance(self, point):
    return self.point.distance_to(point) - self.radius

  def get_normal(self, point):
    return point.minus(self.point)