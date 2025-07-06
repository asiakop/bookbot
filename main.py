from stats import get_num_words, get_char_counts, sort_on, sort_char_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    book_text = get_book_text(book_path) #books/frankenstein.txt

    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = get_char_counts(book_text)
    sorted_counts = sort_char_counts(char_counts)
    
    for item in sorted_counts: 
        print (f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

# Call main to run the program
main()
