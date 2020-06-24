import datetime

def log(message, level=None, path=None, date_time_format=None):
	date = datetime.datetime.today().strftime(date_time_format)
	with open(path, "a+") as logfile:
		logfile.write(f'{level}\t{date}\t\t{message}\n')
