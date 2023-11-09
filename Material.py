# JuliNator99 - juli.schwers@gmail.com
class Material:
  def __init__(self, color: (float, float, float)):
    self.color = (min(color[0], 1), min(color[1], 1), min(color[2], 1))

  def multiply_color(self, value: float):
    red = self.color[0]
    green = self.color[1]
    blue = self.color[2]
    return Material((red * value, green * value, blue * value))

  def combined_color(self, material):
    red = self.color[0] + material.color[0]
    green = self.color[1] + material.color[1]
    blue = self.color[2] + material.color[2]
    return red * 0.5, green * 0.5, blue * 0.5