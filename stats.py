def get_book_text(book):
    text = (f"{book.read()}")
    return text.split()

def get_num_words(book):
    num_words = len(get_book_text(book))
    print(f"Found {num_words} total words")
    
def get_letter_count(book):
    letters = []
    letters_count = []
    words = get_book_text(book)
    for word in words:
        mixed_letters = word.split()
        letters.append(mixed_letters.lower())
    for letter in letters:
        if letter == "a"
            if letters_count != 0
                letters_count[0] += 1
            else letters_count[0] = 1
        elif