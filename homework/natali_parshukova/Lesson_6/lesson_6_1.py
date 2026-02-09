text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
# print(words)
fin_words = []
for word in words:
    if ',' in word:
        word = word.replace(',', 'ing,')
        # print (word)
    elif '.' in word:
        word = word.replace('.', 'ing.')
        # print(word)
    else:
        word = f'{word}ing'
        # print(word)
    fin_words.append(word)
# print(fin_words)
print(' '.join(fin_words))
