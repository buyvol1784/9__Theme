import re

with open('file.txt', 'r') as file:
    content = file.read()

numbers = re.findall(r'\d+', content)

total_sum = 0

for number in numbers:
    total_sum += int(number)

print(f"Сумма всех чисел в файле: {total_sum}")