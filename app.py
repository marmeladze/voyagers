from modules import authentication as auth

user_name = input("Enter you username:\t")
password = input("Enter you password:\t")

if auth.authenticate_user(user_name, password):
	print("Authentication successfull")
else:
	print("Wrong username or password")


menu = """
		(G) Get geolocation information
		(C) Master chemical reactions
		(N) Take notes
		(S) Search notes
		(R) Read notes
	"""

command = (input(menu)).upper()

# if command == "G":
# 	get_lat_long_info()
# 	process_lat_long_info()
# 	show_results()
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

print(command)



