import sys
import stats

def get_book_text(filepath):
    """Read the entire contents of the text file and return it as a string"""
    with open(filepath, "r") as f: 
        return f.read()


def main(): 
    # check for correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    num_words = stats.get_num_words(book_text)
    print(f"Found {num_words} total words")

    words_freq = stats.get_char_counts(book_text)
    sorted_chars = stats.sort_char_counts(words_freq)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()
