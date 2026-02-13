while True:
    number = int(input('угадай цифру, которую я загадал: '))
    if number == 5:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
        continue
