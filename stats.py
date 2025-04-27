# Function: count all the words in the provided book
def book_word_count(book_str):
    # New list, containing all of the words generated using .split()
    book_wrds = book_str.split()
    # Count how many words there are in the list
    word_numb = len(book_wrds)
    # Return: number of words in the book
    return word_numb