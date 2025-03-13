#this one counts the words in a given text
def count_words(text):
    words = text.split()
    return len(words)
def count_chars(text):
    words = text.lower()
    char_count ={}
    for char in words:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def sorted_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        # Note: no colon after "char" in the key name
        char_list.append({"char": char, "count": count})
    
    def sort_on(dict_item):
        return dict_item["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list