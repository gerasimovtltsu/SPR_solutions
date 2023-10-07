def plus_number(number):
    try:
        return 2 + number
    except Exception:
        return "Ожидаемый тип данных - число!"

print(plus_number(1))
print(plus_number("abc"))