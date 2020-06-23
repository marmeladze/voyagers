import pydoc
import datetime as dt
from modules import gutenberg_sdk as gsdk
from modules import commons as com 
from modules import authentication as auth

def main_page_story(app):
	menu = """
	(GEO) Get geolocation information
	(CHEM) Master chemical reactions
	(TN) Take notes
	(SN) Search notes
	(RN) Read notes
	(SB) Search Books
	(RB) Read Book  
	"""	
	command = (com.get_input(menu)).upper()




def auth_user_story(app):
	username = com.get_input("Enter username")
	password = com.get_input("Password")
	user = auth.authenticate_user(username, password)
	if user:
		app.session.variables['user_name'] = username
		app.session.variables['last_login'] =  dt.datetime.now()
		app.logger.log("Successfull login: {username}")
	else:
		print("Wrong username or password")
		app.logger.log(f"Unsuccessfull login attempt: {username}")
	return app


# terms => create search url => search => books 
# path => get book page url => get book page  => document url 
# document_url => get document url => get_document => text 
def search_book_at_gutenberg_story(app):
	term = com.get_input("Search")
	search_url = gsdk.create_search_url(term)
	books = gsdk.search(search_url)
	text = com.build_results(books)
	pydoc.pager(text)
	return app

def get_book_from_gutenberg_story(app):
	path = com.get_input("Book ID")
	book_url = gsdk.create_book_page_url(path)
	document_path = gsdk.get_book_page(book_url)
	document_url = gsdk.create_document_url(document_path)
	document = gsdk.get_document(document_url)
	pydoc.pager(document)
	return app