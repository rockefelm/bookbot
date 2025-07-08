import sys
from stats import word_count, count_characters_by_type, sort_characters_by_frequency
def get_book_text(book_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        book_path (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()
    
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {word_count(get_book_text(sys.argv[1]))} total words")
print("--------- Character Count -------")
sorted_characters = sort_characters_by_frequency(count_characters_by_type(get_book_text(sys.argv[1])))
for character, count in sorted_characters:
    print(f"{character}: {count}")
print("============= END ===============")