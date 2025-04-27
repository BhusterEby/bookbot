# Function: count all the words in the provided book
def book_word_count(book_str):
    # New list, containing all of the words generated using .split()
    book_wrds = book_str.split()
    # Count how many words there are in the list
    word_numb = len(book_wrds)
    # Return: number of words in the book
    return word_numb

# Function: count each character in the provided book
def book_char_count(str_book):
    # Empty dictionary, to store the data in
    char_dict = {}
    # Converting the book's letters to lowercase using .lower()
    lw_str_book = str_book.lower()
    # For loop: for each individual character in the book's string
    for char in lw_str_book:
        # Check if the character already exists in the dictionary
        if char in char_dict:
            # If it is, update the key's value
            char_dict[char] = char_dict[char] + 1
        else:
            # If it isn't, create a new one
            char_dict[char] = 1
    # Return: dictionary filled with counted characters
    return char_dict