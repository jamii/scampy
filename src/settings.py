from server import Server, GMailServer
import getpass

server = GMailServer(getpass.getuser(), getpass.getpass())

logger = server
