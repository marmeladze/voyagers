from collections import namedtuple

Logger = namedtuple("Logger", ['path', 'log'])
Session = namedtuple("Session", ["variables"])
Application = namedtuple("Application", ['name', 'logger', 'session'])
