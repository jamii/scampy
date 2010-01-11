from os import listdir

classifiers = dict( [(scam, ('scams/%s/db' % scam)) for scam in listdir('scams')] )

responses = dict( [(scam, listdir(('scams/%s/responses' % scam))) for scam in listdir('scams')] )

replied = # bloom filter of email addresses, load from data file
