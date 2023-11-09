# JuliNator99 - juli.schwers@gmail.com
from Camera import Camera
from Scene import *


class DefaultRenderer:
  __min_distance = 0.01
  __max_distance = 50.0

  def __init__(self, camera: Camera, scene: Scene):
    self.__camera = camera
    self.__scene = scene

  def __compute_intersection(self, ray: Ray, distance: float = __max_distance):
    iterations = 0
    total_distance = 0.0
    object_to_distance = self.__scene.nearest_distance(ray.interpolate(total_distance))
    start_object = object_to_distance[0]

    while (self.__min_distance < object_to_distance[1] < distance or start_object is object_to_distance[0]) and object_to_distance[1] > 0.0:
      total_distance += abs(object_to_distance[1])
      object_to_distance = self.__scene.nearest_distance(ray.interpolate(total_distance))
      iterations += 1

      if total_distance >= self.__min_distance: start_object = None

    point = None
    if object_to_distance[1] < self.__min_distance: point = ray.interpolate(total_distance)
    return Intersection(object_to_distance[0].material,
                        point,
                        object_to_distance[0].get_normal(ray.interpolate(total_distance)),
                        ray,
                        iterations)

  def compute(self, ray: Ray, total_reflections: int, reflections: int = 0):
    intersection = self.__compute_intersection(ray)

    if intersection.point is not None:
      material = intersection.material
      dot_product = intersection.intersection_normal.dot(ray.direction.reversed())
      light_intensity = max(dot_product, 0)

      ambient = material.color

      if reflections > 0:
        reflection_direction = intersection.from_ray.direction.reflect_using(intersection.intersection_normal)

        ambient_material = self.compute(Ray(intersection.point, reflection_direction), total_reflections, reflections - 1)

        ambient = material.combined_color(ambient_material)

      material = Material(ambient)
      return material.multiply_color(light_intensity)
    else:
      return Material((0.0, 0.0, 0.0))

  def render(self, pixel: (float, float), reflections: int = 0):
    ray = self.__camera.get_ray(pixel)

    return self.compute(ray, reflections, reflections)