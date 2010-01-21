from config import server, logger
from classify import classify
from data import contacted, reponses
import util

def run():
  for message in server.messages():
    if contacted.get(message['from']):
      logger.log("contacted", message)
    else:
      scam = classify(message)
      if scam:
        response = util.read(random.choice(responses[scam]))
        server.reply(message, response)
        contacted.set(message['from'])
        logger.log("classified", clas, message, response)
      else:
        logger.log("unclassified", message)
      
if __name__ == '__main__':
  run()
