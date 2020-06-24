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
		response += f'Author:\t\t{result["title"]}\n'
		response += f'Author:\t\t{result["author"]}\n'
		response += f'URL:   \t\t{result["link"]}\n'
	return response


def normalize_text(text):
	return text.replace(' ', '-')
 