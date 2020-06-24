from collections import namedtuple

Logger = namedtuple("Logger", ['log'])
Session = namedtuple("Session", ["variables"])
Settings = namedtuple("Settings", ['editor_lines', 'notes_folder', 'logs_folder', 'date_format', 'date_time_format'])
Application = namedtuple("Application", ['name', 'logger', 'session', 'mappings', 'settings'])
Command = namedtuple("Command", ["bucket"])