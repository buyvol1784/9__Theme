import re

# Открываем файл для чтения
with open('file.txt', 'r') as file:
    content = file.read()

# Используем регулярное выражение для поиска всех чисел в файле
numbers = re.findall(r'\d+', content)

# Инициализируем сумму чисел
total_sum = 0

# Считаем сумму чисел
for number in numbers:
    total_sum += int(number)

# Выводим результат
print(f"Сумма всех чисел в файле: {total_sum}")