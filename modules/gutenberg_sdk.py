import requests
from bs4 import BeautifulSoup

search_url = "http://www.gutenberg.org/ebooks/search/?query="
base_url = "http://www.gutenberg.org"


def create_search_url(terms):
	"""
	Given string terms, returns a search query url for gutenberg

	>>>create_search_url("Das Kapital")
	"http://www.gutenberg.org/ebooks/search/?query=Das Kapital"
	"""
	return f'{search_url}{terms.replace(" ","+")}'

def create_book_page_url(path):
	return f'{base_url}{path}'

def create_document_url(path):
	return f'{base_url}{path}'

def search(url):
	resp = requests.get(url)
	results = []
	if resp.ok:
		soup = BeautifulSoup(resp.text, "html.parser")
		items = soup.select("li.booklink")
		if len(items) > 0:
			for item in items:
				anchor = item.find("a", class_="link")
				link = anchor.get("href")
				title = anchor.find("span", class_="title").get_text()
				author = anchor.find("span", class_="subtitle").get_text()
				data = dict(link=link, title=title, author=author)
				results.append(data)
			print(f"{len(items)} results found")
			return results
		else:
			print("Zero results found")
	else:
		print("Error while connecting to url -> {url}")


def get_book_page(book_page_url):
	resp = requests.get(book_page_url)
	if resp.ok:
		soup = BeautifulSoup(resp.text, "html.parser")
		table = soup.find("table", class_="files")
		urls = table.find_all("a", class_="link", title="Download")
		return next(filter(lambda e: e.get("type").find('plain') > 0, urls)).get("href")


def get_document(document_url):
	print(f'[x] Fetching document: {document_url}')
	resp = requests.get(document_url)
	if resp.ok:
		return resp.text
