from collections import Counter

def count_words(book_string: str) -> int:
    """
    Return the number of words in *book_string*.
    Splitting on whitespace is enough for a simple word count.
    """
    # ``split()`` without an argument splits on any run of whitespace
    return len(book_string.split())


def count_chars(book_string: str) -> Counter:
    """
    Return a Counter mapping each character (lower‑cased) to its frequency.
    """
    return Counter(c.lower() for c in book_string if c.isalpha())


def sort_counts(char_count: Counter):
    """
    Return a list of tuples `(char, count)` sorted by *count* descending.
    The returned list can be printed or processed further.

    ``Counter`` objects are dict‑like, so we use the built‑in
    :func:`sorted` to order the items.
    """
    # ``sorted`` returns a new list; it does **not** modify the Counter in place
    return sorted(char_count.items(), key=lambda kv: kv[1], reverse=True)
