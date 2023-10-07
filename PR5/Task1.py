# Вариант 1

f = open('read_file.txt', 'r', encoding='utf8')
print(f.read())

# Вариант 2

with open('read_file.txt', 'r', encoding='utf8') as f2:
    print(f2.read())