def word_counter(words):
    text = words.split()
    return len(text)

def letter_counter(words):
    dict = {}

    for letter in words:
        my_letter = letter.lower()
        if my_letter.isalpha():
            dict[my_letter] = dict.get(my_letter, 0) + 1
    
    return dict

def dict_sorter(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)