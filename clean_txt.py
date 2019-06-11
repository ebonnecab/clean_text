#! usr/bin/env python3

#load text
def read_file(file):
    with open(file) as f:
        text = f.read()
    return text

from nltk import word_tokenize

def create_tokens(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    return tokens

import string

def strip_tokens(tokens):
    table = str.maketrans('', '', string.punctuation)
    stripped = [word.translate(table) for word in tokens]
    words = [word for word in stripped if word.isalpha()] 

    return words

def write_data(file, corpus):
    with open(file, 'w+') as f:
        for post in corpus:
            f.write(post + " ")
            
if __name__ == "__main__":
    txt = read_file("Alice_Wonder.txt")
    tokens = create_tokens(txt)
    words = strip_tokens(tokens)
    # print(words)
    write_data('clean_alice.txt', words)
   
    