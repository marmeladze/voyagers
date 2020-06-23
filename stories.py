import pydoc
from modules import gutenberg_sdk as gsdk
from modules import commons as com 


def search_book_at_gutenberg_story():
	term = com.get_search_term()
	search_url = gsdk.create_search_url(term)
	books = gsdk.search(search_url)
	text = com.build_results(books)
	pydoc.pager(text)
	