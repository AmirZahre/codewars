def duplicate_encode(word):
    word_lower = word.lower()

    new_word = ""

    for letter in word_lower:
        if word_lower.count(letter) > 1:
            new_word += ")"
        else:
            new_word += "("
    
    return new_word

print (duplicate_encode("(( @"))