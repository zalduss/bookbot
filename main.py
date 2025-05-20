
from stats import get_num_words, get_num_chars, format_content
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        data = f.read()
    return data



content = get_book_text(filepath)
total_words = get_num_words(content)
format_content(content, total_words)




