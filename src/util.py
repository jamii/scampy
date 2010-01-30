def read(filename):
  file = open(filename)
  text = file.read()
  file.close()

  return text

def limit(n, text):
  if len(text) > n:
    return text[:n] + ' ......'
  else:
    return text

class ConsoleLogger():
  def __init__(self):
    pass
  
  def log(self, *args):
    print
    for arg in args:
      print limit(100, str(arg))
