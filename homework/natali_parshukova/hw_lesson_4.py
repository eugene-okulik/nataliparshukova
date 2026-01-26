my_dict = {}
my_dict['tuple'] = (5, None, 'test', True, 1.11)
my_dict['list'] = [3, None, 'list', False, 4.44]
my_dict['dict'] = {'one': 'value1', 'two': 'value2', 'three': 'value3', 4: 4, 5: 5}
my_dict['set'] = {2, 7, 9, 'aaa', 'bbb'}

print("словарь в начале: ", my_dict)

print('последний элемент в tuple: ', my_dict['tuple'][-1])

my_dict['list'].append(5.55)
print("добавлен элемент 5.55 в list: ", my_dict['list'])
my_dict['list'].pop(1)
print("удалён второй элемент из list: ", my_dict['list'])

my_dict['dict']['i am a tuple'] = 'the same'
print("добавлен элемент 'i am a tuple' с ключом в dict: ", my_dict['dict'])
my_dict['dict'].pop('three')
print("удален элемент из dict: ", my_dict['dict'])

my_dict['set'].add('ccc')
print("добавлен элемент 'ccc' в set:", my_dict['set'])
my_dict['set'].remove('aaa')
print("удален элемент 'aaa' из set: ", my_dict['set'])

print("словарь после преобразований: ", my_dict)
