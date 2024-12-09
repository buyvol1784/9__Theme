from collections import Counter

with open('input.txt', 'r') as file_in, open('output.txt', 'w') as file_out:
    for line in file_in:
        words = line.split()

        word_count = Counter(words)

        most_common_word, count = word_count.most_common(1)[0]

        file_out.write(f"Самое часто встречаемое слово в строке: {most_common_word}, количество повторений: {count}\n")

print("Готово! Проверьте файл 'output.txt' для результатов.")