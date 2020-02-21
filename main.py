def addition(x, y):
  print(f'addition called with {x}, {y}')
  return x = y


def test_addition():
  assert addition(3, 5) == 8
