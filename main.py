import os

def get_book_text(bookLoc):
  with open(bookLoc) as b:
    book_contents = b.read()
  return book_contents

def main():
  frank = os.path.expanduser('~/bookbot/bookbot/books/frankenstein.txt')  
  text = get_book_text(frank)
  print(text)

main()  

