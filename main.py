def main():
    book_path = "books/frankenstein.txt"
    file_contents = read_pages(book_path)

    print("--- Begin report of books/frankenstein.txt ---")
    print()
    print(f"The word count of the books is {count_words(file_contents)} words.")
    letter_dict, char_count = count_characters(file_contents)
    print(f"There are {char_count} characters.")
    print()
    for key in letter_dict:
        print(f"The letter {key} appeared {letter_dict[key]} times.")

def read_pages(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def count_characters(file_contents):
    char_count = 0
    letter_dict = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
    words = file_contents.split()
    for word in words:
        lower_case_string = word.lower()
        character_list = list(lower_case_string)
        for char in character_list:
            char_count += 1 
            if char in letter_dict:
                letter_dict[char] += 1

    return letter_dict, char_count

main()

