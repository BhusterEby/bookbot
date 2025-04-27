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

# Function: key for the .sort() command
def sort_key(dict):
    # Return: variable used in the "num" key
    return dict["num"]

# Function: sorts a dictionary of counted characters
def book_dict_sort(dict_count):
    # Empty list, to sort the dictionaries into
    sort_list = []
    # For loop: for each key in the dictionary
    for letter in dict_count:
        # Form a new dictionary, using both the key and its value as two separate values
            # Then add it to the list
        sort_list.append({"char": letter, "num": dict_count[letter]})
    # Organizes the list using .sort()
        # In reverse to sort from max to min, sort by the sort_key function
    sort_list.sort(reverse=True, key=sort_key)
    # Return: sorted list of counted characters
    return sort_list

# Function: prints out a book report
def book_report(path_way, word_num, char_list):
    # 1st set: introduce the report, and the path to the book
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_way}...")
    # 2nd set: provide the total amount of words
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    # 3rd set: provide the total count of each character/letter
    print("--------- Character Count -------")
    # For loop: for each counted item in the list
    for c in char_list:
        # Check if the character is an alphabetical letter
        if c["char"].isalpha():
            # If so, print it
            print(f"{c["char"]}: {c["num"]}")
    # End the book report
    print("============= END ===============")