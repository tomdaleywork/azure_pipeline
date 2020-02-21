from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
  value = addition(5, 10)
  return f'<html><body><h1 id="value">{value}</h1></body></html>'


def addition(x, y):
  print(f'addition called with {x}, {y}')
  return x + y
