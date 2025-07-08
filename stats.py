def word_count(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_characters_by_type(text):
    character_count = {}
    for char in text.lower():
        character_count[char] = character_count.get(char, 0) + 1
    return character_count

def sort_characters_by_frequency(character_count):
    """
    Sorts characters by their frequency in descending order.
    
    Args:
        character_count (dict): A dictionary with characters as keys and their counts as values.
        
    Returns:
        list: A list of tuples sorted by frequency in descending order.
    """
    return sorted(character_count.items(), key=lambda item: item[1], reverse=True)