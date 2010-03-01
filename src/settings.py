from server import Mail, GMail
import util

server = GMail(raw_input('GMail address: '), raw_input('GMail password: '))

logger = util.ConsoleLogger()
