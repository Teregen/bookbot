import sys

def get_book_text(book_path) -> str:
    with open(book_path, "r") as text:
        return text.read()
    
from stats import count_words

from stats import count_characters

from stats import sort_chars
    
def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        word_count = count_words(book_text)
        sorted_dict = sort_chars(count_characters(book_text))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words.")
        print("--------- Character Count -------")
        for char_dict in sorted_dict:
            char = char_dict["char"]
            count = char_dict["count"]
            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    

main()


        
