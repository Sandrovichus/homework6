my_dict = {'Имя': 'Олег', 'Фамилия': 'Сидоров', 'Год рождения': '2000', 'Город': 'Ижевск'}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Город'))
print('Not existing value:', my_dict.get('Профессия'))
my_dict.update({'Отчество': 'Викторович', 'Профессия': 'разработчик'})  # добавили 2 пары ключ-значение
print('Deleted value:', my_dict.pop('Город'))
print('Modified dictionary:', my_dict)
print()

my_set = {2, 1.5, False, (2, 45, True, 'Привет'), 'Пока', 2, 58, 1.5, True, True}
print('Set:', my_set)
my_set.update({1000, 'дом'})  # добавили 2 элемента
my_set.remove(True)           # удалили 1 элемент
print('Modified set:', my_set)
