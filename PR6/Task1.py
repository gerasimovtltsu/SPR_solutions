# Вариант полный

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

number = int(input("Введите число: "))
print(is_even(number))

# Вариант короткий

def is_even2(n):
    return n % 2 == 0

number2 = int(input("Введите число: "))
print(is_even2(number2))