from termcolor import colored

def get_input(hint):
	return input(f"{hint}:\t")

def get_help():
	return """
	To do something do anything
	Lorem ipsum dolor sit amet
	USAGE: python script.py
	"""

def show_gutenberg_book_search_results(results):
	response = ""
	for result in results:
		response += f'{"*"*50}\n'
		response += f'Author:\t\t{result["title"]}\n'
		response += f'Author:\t\t{result["author"]}\n'
		response += f'URL:   \t\t{result["link"]}\n'
	return response

def normalize_text(text):
	return text.replace(' ', '-')

def colorize_word(word, color="red"):
    return colored(word, color, attrs=['bold'])

def highlighted_word(text, word, highlighter=colorize_word):
    frequency = text.count(word)
    text = text.replace(word, highlighter(word), frequency)
    return text

def show_note_search_results(results):
    response = ""
    for result in results:
        response += f'{result["document"]}@{result["line_no"]: {<25}}\t\t'
        response += f'{highlighted_word(result["line"], result["pattern"])}\n'
    return response

