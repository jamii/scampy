def read(filename):
  file = open(filename)
  text = file.read()
  file.close()

  return text


