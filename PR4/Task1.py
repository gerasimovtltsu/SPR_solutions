lst = []

cnt = int(input("Введите количество элементов списка: "))

for i in range(cnt):
    lst.append(input(f"Введите {i} элемент:"))

lst.reverse()
print(lst)