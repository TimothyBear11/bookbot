import os
from stats import count_words, count_chars

def get_book_text(bookLoc):
  with open(bookLoc) as b:
    book_contents = b.read()
  return book_contents

def main():
  frank = os.path.expanduser('~/bookbot/books/frankenstein.txt')  
  text = get_book_text(frank)
  numWords = count_words(text)
  print(f"Found {numWords} total words")
  charCount = count_chars(text)
  print(charCount)


main()  

