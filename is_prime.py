def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Пример использования функции
num = int(input("Введите число: "))
if is_prime(num):
    print(f"{num} является простым числом.")
else:
    print(f"{num} не является простым числом.")