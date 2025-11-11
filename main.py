import sys
from stats import get_num_words, get_letter_count, dict_sort

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in sorted(letter_count.items(), key=dict_sort, reverse=True):
        print(f"{k}: {v}")
    print("============= END ===============")
    
def get_book_text(path):
    with open(path) as book:
        return book.read()

main()