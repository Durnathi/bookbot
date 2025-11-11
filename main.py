from stats import get_num_words, get_letter_count, dict_sort

def main ():
    book_path = "books/frankenstein.txt"
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