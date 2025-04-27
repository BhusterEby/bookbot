from stats import book_word_count
from stats import book_char_count
from stats import book_dict_sort
from stats import book_report
import sys

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
        #story_string = get_book_text("books/frankenstein.txt")
    # Check if the command has two inputs or not
    if len(sys.argv) != 2:
        # If it doesn't, print instructions
        print("Usage: python3 main.py <path_to_book>")
        # Then exit the program with status code 1
        sys.exit(1)
    else:
        # Get the book path
        book_path = sys.argv[1]
        # Get the story as a variable
        story_string = get_book_text(book_path)
        # Get the word count
        num_words = book_word_count(story_string)
        # Get the character count
        story_dict = book_char_count(story_string)
        # Sort the character count
        sort_story_dict = book_dict_sort(story_dict)
        # Generate the book report
        book_report(book_path, num_words, sort_story_dict)

# Run
main()