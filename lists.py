lists = [3,5,7,9,10.5]
print(lists)
lists.append('Python')
print(f'Длина списка: {len(lists)}')
print(lists[0])
print(lists[-1])
# Напечатайте элементы списка со второго по четвертый включительно
print(lists[1:4]) # второй по порядку или по индексу?
lists.remove('Python')