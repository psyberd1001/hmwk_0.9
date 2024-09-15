def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    same_words_1 = [s.lower() for s in other_words]
    for i in same_words_1:
        if i in root_word or root_word in i:
            same_words.append(i)
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))