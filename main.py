from stats import count_words
from stats import count_chars, sorted_list
import sys
#this gets the text from the file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
#this one counts the words in a given text
def count_words(text):
    words = text.split()
    return len(words)
#get the text and count the words
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        word_count = count_words(text)
        char_counts = count_chars(text)
        sorted_chars = sorted_list(char_counts)
    
        # Print the report header
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        
        # Print word count section
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        
        # Print character count section
        print("--------- Character Count -------")
        
        # Print each character and its count, but only for alphabetic characters
        for char_dict in sorted_chars:
            char = char_dict["char"]  # Make sure this matches your key name!
            count = char_dict["count"]
            
            # Only print alphabetic characters
            if char.isalpha():
                print(f"{char}: {count}")
        
        # Print the report footer
        print("============= END ===============")

main()
    
