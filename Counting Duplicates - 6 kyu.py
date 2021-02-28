def duplicate_count(text):

    text_new = list(text.lower())

    x = 0
    for letter in text_new:
        if text_new.count(letter) > 1:
            text_new = [t for t in text_new if t != letter]
            x += 1


    return x
            

print(duplicate_count("Indivisibilities"))