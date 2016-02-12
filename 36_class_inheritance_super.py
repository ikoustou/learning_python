class Book():
	def __init__(self, title, author, pages):
		self.title=title
		self.author=author
		self.pages=pages


class Ebook(Book):
	"""docstring for Ebook"""
	def __init__(self, title, author, pages, format_):
		super ().__init__(title, author, pages)
		self.format_=format_


ebook1=Ebook('The Catcher in the Rye', 'J. Salinger', 214 , 'pdf')

print(ebook1.title)
print(ebook1.author)
print(ebook1.pages)
print(ebook1.format_)
		