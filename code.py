#########################
# !!! SOLUTION CODE !!! #
#########################



from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
  title = "No title was given."
  author = "No author was given."
  price = 0
  
  def __init__(self, title=title, author=author, price=price):
    self.title = title
    self.author = author
    self.price = price

  def display(self):
    print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}")

title=input()
