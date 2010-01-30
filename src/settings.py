from server import Mail, GMail
import getpass
import util

# server = GMail(getpass.getpass('GMail address: '), getpass.getpass('GMail password: '))
server = GMail('', '')

logger = util.ConsoleLogger()
