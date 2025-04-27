from stats import book_word_count
from stats import book_char_count
from stats import book_dict_sort
from stats import book_report

# Function: make a string of the provided .txt file (book) location
def get_book_text(fp):
    # Empty string, to store the book's contents in
    file_contents = ""
    # With block: opens the file
    with open(fp) as f:
        # Import the entire contents of the file to the string using .read()
        file_contents = f.read()
    # Return: string containing the entire book
    return file_contents

# Function: main
def main():
    # Get the story as a variable
    story_string = get_book_text("books/frankenstein.txt")
    # Get the word count
    num_words = book_word_count(story_string)
    # Get the character count
    story_dict = book_char_count(story_string)
    # Sort the character count
    sort_story_dict = book_dict_sort(story_dict)
    # Generate the book report
    book_report("books/frankenstein.txt", num_words, sort_story_dict)

# Run
main()