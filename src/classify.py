import data
from settings import server

cutoff = 0.95

def classify(text):
  score, scam = max[(classifier.score(text), scam) for (classifier, scam) in data.classifiers.items()]
  if score > cutoff:
    return scam
  else:
    return None

def train():
  for scam in data.scams:
    msgs = server.fetch(folder=scam)
    for key, classifier in classifiers.items():
      for msg in msgs:
        if key == scam:
          classifier.train_ham(msg.as_string())
        else:
          classifier.train_spam(msg.as_string())
    # marks msgs as seen
