#!/usr/bin/env python
# Kurt Spindler
# version 1.0
import ConfigParser as cp

class ServerConfig(cp.ConfigParser, object):
    #Server
    IS_DEV = property(lambda self: self.get('server', 'deployment') == 'dev')
    IS_STAGE = property(lambda self: self.get('server', 'deployment') == 'stage')
    IS_PROD = property(lambda self: self.get('server', 'deployment') == 'prod')
    PORT = property(lambda self: self.getint('server', 'port'))
    #Database
    DB_NAME = property(lambda self: self.get('database', 'dbname'))
    DB_USER = property(lambda self: self.get('database', 'username'))
    DB_PASSWD = property(lambda self: self.get('database', 'passwd'))

    def __init__(self, fp = 'app.conf'):
        # Default is to actually read from ./app.conf
        # Set to None in order to not actually read.
        super(ServerConfig, self).__init__()
        if fp is not None:
           self.read(fp)

