import os
from stats import count_words, count_chars, sort_counts

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
  sortedCounts = sort_counts(charCount)
  for char, count in sortedCounts:
      if char.isalpha():
          print(f"{char}: {count}")


main()
