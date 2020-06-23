def get_input(hint):
	return input(f"{hint}:\t")

def get_help():
	return """
	To do something do anything
	Lorem ipsum dolor sit amet
	USAGE: python script.py
	"""

def build_results(results):
	response = ""
	for result in results:
		response += f'{"*"*50}\n'
		response += f'Author:\t\t{result["author"]}\n'
		response += f'URL:   \t\t{result["link"]}\n'
	return response



def resolve_command_to_story(command, bucket):
	"""(GEO) Get geolocation information
	(CHEM) Master chemical reactions
	(TN) Take notes
	(SN) Search notes
	(RN) Read notes
	(SB) Search Books
	(RB) Read Book
	"""
