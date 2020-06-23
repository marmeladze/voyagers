import datetime
import config
from containers import Logger, Session, Application
import boot
from stories import (
	auth_user_story,
	# main_page_story,
	search_book_at_gutenberg_story,
	get_book_from_gutenberg_story,
	)

path = boot.prepare_logger(logs_path=config.logs_path, date_format=config.date_format)

def log(message, level="INFO", path=path):
	date = datetime.datetime.today().strftime(config.date_time_format)
	with open(path, "a+") as logfile:
		logfile.write(f'{level}\t{date}\t\t{message}\n')
	return


logger = Logger(path=config.logs_path, log=(lambda msg: log(msg)))
session = Session(variables={'last_login': ''})
app = Application(name="Time Traveler's Terminal", logger=logger, session=session)


auth_user_story(app)



# if auth.authenticate_user(user_name, password):
# 	print("Authentication successfull")
# else:
# 	print("Wrong username or password")


# if command == "SB":
# 	search_book_at_gutenberg_story()
# elif command == "RB":
# 	get_book_from_gutenberg_story() 
# elif command == "C":
# 	ask_reaction_details()
# 	show_results()
# elif command == "N":
# 	note_taker()
# elif command == "S":
# 	ask_keywords()
# 	show_results()
# elif command == "R":
# 	ask_for_input()
# 	show_note()
# else:
# 	print("Unknown command")
