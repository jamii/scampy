import imaplib
import smtplib
import email.parser
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Mail():
  def __init__(self, user, password, imapAddress, smtpAddress):
    pass

  def connect(self):
    pass

  def fetch(self, folder='Inbox'):
    # Where do we mark messages as seen?
    parser = email.parser.Parser()
    self.imap.select(folder)
    status, uids = self.imap.search(None, 'UNSEEN')
    uids = uids[0].replace(' ',',')
    status, data = self.imap.fetch(uids, '(RFC822)')
    self.imap.close()
    return [(uid.split()[0], parser.parsestr(mail)) for (uid, mail) in data[::2]]

  def send(self, message):
    self.smtp.sendmail(self.user, message['To'], message.as_string())  

  def reply(self, message, text):
    reply = MIMEMultipart()
    reply['From'] = self.user
    reply['To'] = message['From']
    reply['Subject'] = "RE: " + message['Subject']
    reply.attach(MIMEText(text))

    self.send(reply)

  def log(self, subject, **args):
    log = MIMEMultipart()
    log['From'] = self.user
    log['To'] = 'logaddress'
    log['Subject'] = "Log: " + subject
    text = "\n\n".join([k + ":\n" + v for k, v in args])
    log.attach(MIMEText(text))

    self.send(log)

  def disconnect(self):
    self.imap.logout()
    self.smtp.quit()

  def seen(self, uid, folder='Inbox'):
    self.imap.select(folder)
    self.imap.store(uid, '+FLAGS', r'\Seen')
    self.imap.close()


class GMail(Mail):
  def __init__(self, user, password):
    self.user = user
    self.password = password

  def connect(self):
    self.imap = imaplib.IMAP4_SSL('imap.gmail.com',993)
    self.imap.login(self.user, self.password)
        
    self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
    self.smtp.ehlo()
    self.smtp.starttls()
    self.smtp.ehlo()
    self.smtp.login(self.user, self.password)
