from os import listdir
import cPickle as pickle

classifiers = []
responses = []
replied = set()

def load():
  classifiers = dict( [(scam, ('scams/%s/db' % scam)) for scam in listdir('scams')] )
  responses = dict( [(scam, listdir(('scams/%s/responses' % scam))) for scam in listdir('scams')] )
  replied = pickle.load('data/replied')

def save():
  pickle.dump(replied, 'data/replied')
