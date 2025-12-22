# This script reads the text of a book, cleans it by removing punctuation, digits, and single-letter words, converts all words to lowercase, counts how often each word appears, and prints the word frequencies with a specific count for "Alice".

import re
from collections import Counter

alice_book = open(r"C:\Users\Bar Shenig\OneDrive\Desktop\pg11.txt", mode='r', encoding='utf8')

def reading_content():
    read_alice_book = alice_book.read()
    return read_alice_book

def clean_text_and_return_list(read_alice_book):
    clean_text = re.sub(r"[^A-Za-z\s]", " ", read_alice_book)
    clean_text = re.sub(r"\s+", " ", clean_text).strip()
    clean_text = clean_text.lower()
    clean_text = [word for word in clean_text.split() if len(word) > 1]
    return clean_text

def word_frequency(words_list):
    word_count = Counter(words_list)
    sorted_word_count = dict(word_count.most_common())
    return sorted_word_count

read_alice_book = reading_content()
clean_text = clean_text_and_return_list(read_alice_book)
freq_dict = word_frequency(clean_text)

print(freq_dict)
print("The word Alice is presented", freq_dict['alice'], "times")
