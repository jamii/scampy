from os import listdir
import cPickle as pickle
from spambayes import hammie

scams = listdir('scams')
classifiers = {}
responses = {}
contacted = set()

def classifier(scam, mode='c'):
  # Might have to first create the folder/file
  return hammie.open(('scams/%s/db' % scam), mode)

def load():
  classifiers = dict( [(scam, classifier(scam)) for scam in scams] )
  responses = dict( [(scam, listdir(('scams/%s/responses' % scam))) for scam in scams] )
  contacted = pickle.load('data/contacted')

def save():
  for scam, classifier in classifiers:
    classifier.store()
  pickle.dump(contacted, 'data/contacted')
