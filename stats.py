def count_words(book_text):
    return len(book_text.split())
# split() separates the text into words based on whitespace.  Len() counts the number in a list, in this case, words.

def count_characters(book_text): #book_text is a string from the main.py file
    ############### Count the number of characters in a book ###############
    book_text = book_text.lower() #lower() makes all the characters lowercase
    char_count = {} #dictionary to store the count of each character, empty creation
    for char in book_text: #char is empty variable, like i, a placeholder. book_text is now a list of each character separate.
        if char in char_count: #if the character is already in the dictionary, then plus 1
            char_count[char] += 1 #char_count is the dictionary, char is the key, and += 1 adds one to the value
        else:
            char_count[char] = 1 #if the character is not in the dictionary, then add it to the dictionary with a value of 1
    ############### End of counting the number of characters in a book ###############
    return char_count

def sort_chars(char_dict):
    char_list = [{"char": char, "count": count} for char, count in char_dict.items()]
               #Makes empty list, {} is dictionary part, #char is the key, count is the value, and items() returns a list of tuples
               #so this way we know the names of the key and values
    char_list.sort(reverse=True, key=lambda d: d["count"]) #reverse True means biggest to smallest.
                                 #lambda is like a small one time use function, d is the dictionary, and d["count"] is the value
                                 #gonna need to study this more.
    return char_list
    
