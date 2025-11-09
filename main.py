from stats import get_book_text, get_num_words, get_letter_count

def main ():
    with open("books/frankenstein.txt") as file:
        get_num_words(file)

main()