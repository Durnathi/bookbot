def get_num_words(book):
    words = book.split()
    return len(words)
    
def get_letter_count(book):
    letters = {}
    for letter in book:
        lowered = letter.lower()
        if lowered.isalpha():
            if lowered in letters:
                letters[lowered] += 1
            else:
                letters[lowered] = 1
    return letters
    
def dict_sort(key):
    return key[1]