# Создать строку равную всем элементам введенной строки с четными
# индексами. (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого, индексы 0,2,4,6....)

a = input('Введите прозвольное слово или символы: ')

b = a[0::2]

print(f'Четные сиволы в этой строке будут: {b}')