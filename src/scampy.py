from settings import server, logger
from classify import classify
import data
import random
import util

def run():
  data.load()
  server.connect()
  for (uid, message) in server.fetch()[:50]:
    try:
      #if message['from'] in data.contacted:
      #  logger.log("contacted", message)
      #else:
        scams = classify(message)
        if scams:
          scam = random.choice(scams)
          response = random.choice(data.responses[scam])
        else:
          response = random.choice(data.default)
        server.reply(message, response)
        data.contacted.add(message['from'])
        logger.log("classified", str(scams), message.as_string(), response)
        server.seen(uid)
    except Exception, e:
      print e
  server.disconnect()
  data.save()
      
if __name__ == '__main__':
  run()
