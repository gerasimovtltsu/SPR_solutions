number = int(input())

for i in range(11):
    if number <= 0:
        print("Число должно быть положительным")
        break
    print(number * i, end=' ')