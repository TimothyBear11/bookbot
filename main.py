# main.py
import sys
from stats import count_words, count_chars, sort_counts

def get_book_text(path: str) -> str:
    """Return the entire contents of *path* as a single string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    char_counter = count_chars(book_text)
    sorted_counts = sort_counts(char_counter)

    # Print top 10 most common letters
    for char, cnt in sorted_counts[:10]:
        print(f"{char}: {cnt}")

if __name__ == "__main__":
    main()
