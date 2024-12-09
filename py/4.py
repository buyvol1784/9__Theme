def censor_text(file_name, stop_words_file):
    with open(stop_words_file, 'r') as stop_words_file:
        stop_words = stop_words_file.read().split()

    with open(file_name, 'r') as file:
        text = file.read()

    for word in stop_words:
        text = text.replace(word.lower(), '*' * len(word))

    print(text)

censor_text('text.txt', 'stop_words.txt')