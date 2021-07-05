# Counting words line by line.
def clean_text(text):
    text = text.replace("\n", " ")
    joined_text = ''.join(c for c in text if c.isalnum() or c == " ")
    return joined_text.lower().strip().split()

def add_to_dictionary(dictionary, text):
    for word in text:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

def show_result(dictionary):
    for key in sorted(dictionary):
        print(key, ":", dictionary[key])    

with open("./text-files/blakepoems.txt") as text_file:
    dictionary = dict()
    for line in text_file:
        if line != "\n":
            splitted_text_clear = clean_text(line)
            dictionary = add_to_dictionary(dictionary, splitted_text_clear)
    
    show_result(dictionary)