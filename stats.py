from collections import Counter

def count_words(bookString):
  words = bookString.split()
  numWords = 0
  for word in words:
    numWords += 1
  return numWords  

def count_chars(bookString):
    return Counter(bookString.lower())
