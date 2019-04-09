# Python Abstract Classes

### [HackerRank](www.hackerrank.com)

> Given a Book class and a Solution class, write a MyBook class that does the following:
> Inherits from Book, Has a parameterized constructor taking title, author, and price parameters.
> Implements the Book class' abstract display() method so it prints these 
> *title, a space, and then the current instance's title*,
> *author a space, and then the current instance's author*,
> *price a space, and then the current instance's price*,
>lines.

This one is also somewhat of a given.

## Steps

* Create a MyBook class that inherits from Book
* Initialize with title, author, and price
* Define a method called display that prints the necessary lines

## Code

### Create a MyBook class that inherits from Book

```python
class MyBook(Book):
```

### Initialize with title, author, and price

```python
...
  title = "No title was given."
  author = "No author was given."
  price = 0
  
  def __init__(self, title=title, author=author, price=price):
    self.title = title
    self.author = author
    self.price = price
```

### Define a method called display that prints the necessary lines

```python
def display(self):
    print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}")
```

### Final Code

```python
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
```

## Conclusion

Another good warm up. Appreciate the easy ones but can not wait for more difficult tasks.
