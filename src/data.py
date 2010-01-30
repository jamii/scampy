from os import listdir
from os.path import isdir
import cPickle as pickle
from spambayes import hammie
from util import read

scams = []
classifiers = {}
responses = {}
default = []
contacted = set()

def classifier(scam, mode='c'):
  # Might have to first create the folder/file
  return hammie.open(('scams/%s/db' % scam), mode)

def load():
  global scams, classifiers, responses, default, contacted
  scams = [scam for scam in listdir('scams') if isdir(('scams/%s' % scam))]
  classifiers = dict( [(scam, classifier(scam)) for scam in scams] )
  responses = dict( [(scam, read(('scams/%s/responses' % scam)).split('###')) for scam in scams] )
  default = read('scams/responses').split('###')
  contactFile = open('data/contacted','r')
  contacted = pickle.load(contactFile)
  contactFile.close()

def save():
  for scam, classifier in classifiers:
    classifier.store()
  contactFile = open('data/contacted','w')
  pickle.dump(contacted, contactFile)
  contactFile.close()

if __name__ == '__main__':
  save()
