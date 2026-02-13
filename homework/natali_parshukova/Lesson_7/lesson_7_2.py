words = {'I': 3, 'love': 5, 'Python': 1, '!': 50, 'ёпрст_': 10, 'ну_ваще ': 9}
for key, value in words.items():
    key *= value
    print(key)
