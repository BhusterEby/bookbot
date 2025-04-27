from stats import book_word_count

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
    print(f"{num_words} words found in the document")

# Run
main()