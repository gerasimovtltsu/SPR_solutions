# Вариант 1

f = open("write_file.txt", 'w', encoding="utf8")
text = input("Введите текст для записи в файл: ")
f.write(text)
f.close()

# Вариант 2

text2 = input("Введите текст для записи в файл: ")
with open('write_file.txt', 'w', encoding='utf8') as f2:
    f2.write(text2)