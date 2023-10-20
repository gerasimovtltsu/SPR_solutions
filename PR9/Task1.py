class Figure:
  def perimetr():
    pass

def validate(func):
  def wrapper(*args, **kwargs):
    for arg in args:
      if arg < 0:
        raise ValueError("Значение не может быть отрицательным")
    return func(*args, **kwargs)
  return wrapper

class Rectangle(Figure):
  @validate
  def perimetr(width, height):
    return 2 * (width + height)

print(Rectangle.perimetr(-1, 2))
