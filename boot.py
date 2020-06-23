import os
import datetime as dt


def get_file_path(logs_path, date_format):
	fname = f'{dt.datetime.today().strftime(date_format)}.txt'	
	abs_path = os.path.join(logs_path, fname)
	return abs_path


def initialize_logger(abs_path):
	if not os.path.exists(abs_path):
		open(abs_path, "a+").close()
	return True

def prepare_logger(logs_path, date_format):
	abs_path = get_file_path(logs_path, date_format)
	if initialize_logger(abs_path):
		return abs_path



