# from modules import authentication as auth

# user_name = input("Enter you username:\t")
# password = input("Enter you password:\t")

# if auth.authenticate_user(user_name, password):
# 	print("Authentication successfull")
# else:
# 	print("Wrong username or password")


menu = """
(GEO) Get geolocation information
(CHEM) Master chemical reactions
(TN) Take notes
(SN) Search notes
(RN) Read notes
(SB) Search Books
(RB) Read Book  
"""

from stories import search_book_at_gutenberg_story

command = (input(menu)).upper()
if command == "SB":
	search_book_at_gutenberg_story()

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
