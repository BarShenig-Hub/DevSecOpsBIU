# This script reads the text of a book, cleans it by removing punctuation, digits, and single-letter words, converts all words to lowercase, counts how often each word appears, and prints the word frequencies with a specific count for "Alice".

import re
from collections import Counter

def reading_content(alice_book):
    read_alice_book = alice_book.read()
    return read_alice_book

def clean_text_and_return_list(read_alice_book):
    # Remove all characters that are NOT letters (A-Z, a-z) or whitespace
    # Replaces punctuation, numbers, and special characters with a space
    clean_text = re.sub(r"[^A-Za-z\s]", " ", read_alice_book)
    # Replace multiple consecutive whitespace characters with a single space
    # Then remove leading/trailing whitespace with strip()
    clean_text = re.sub(r"\s+", " ", clean_text).strip()
    clean_text = clean_text.lower()
    clean_text = [word for word in clean_text.split() if len(word) > 1]
    return clean_text

def word_frequency(words_list):
    word_count = Counter(words_list)
    sorted_word_count = dict(word_count.most_common())
    return sorted_word_count


def do_all():
    alice_book = open('alice.txt', mode='r', encoding='utf8')
    read_alice_book = reading_content(alice_book)
    clean_text = clean_text_and_return_list(read_alice_book)
    freq_dict = word_frequency(clean_text)
    first_key = next(iter(freq_dict))
    first_value = freq_dict[first_key]
    print(f'Most common word is "{first_key}", count: {first_value}')
    print("The word Alice is presented", freq_dict['alice'], "times")

do_all()
