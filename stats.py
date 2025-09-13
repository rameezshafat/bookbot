def get_char_counts(text):
    """Return a dictionary with counts of each character in the given text."""
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def get_num_words(book_text):
    """Return number of words in the text"""
    arr = book_text.split()
    return len(arr)
def sort_char_counts(char_counts):
    """
    Convert a dictionary of char counts into a sorted list of dicts.
    Each element has {"char": <letter>, "num": <count>}.
    Only alphabetical characters are included.
    Sorted from highest to lowest count.
    """
    char_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # skip spaces, punctuation, etc.
            char_list.append({"char": char, "num": count})

    # helper function to extract "num" for sorting
    def sort_on(d):
        return d["num"]

    # sort in place, reverse=True for descending
    char_list.sort(key=sort_on, reverse=True)

    return char_list
