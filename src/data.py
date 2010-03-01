from os import listdir
from os.path import isdir
import cPickle as pickle
try:
  # Don't actually need this at the moment
  from spambayes import hammie
except Exception, e:
  print "Couldn't find spambayes, probably don't care"
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
  try:
    contactFile = open('data/contacted','r')
    contacted = pickle.load(contactFile)
    contactFile.close()
  except IOError:
    pass # data/contacted doesnt yet exist, leave contacted as empty set

def save():
  for scam, classifier in classifiers:
    classifier.store()
  contactFile = open('data/contacted','w')
  pickle.dump(contacted, contactFile)
  contactFile.close()

if __name__ == '__main__':
  save()
