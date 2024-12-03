def sum_of_list(n):
    total = 0
    for number in n:
        total += number
    return total
n_input = input("Введите числа через пробел: ")
n_list = list(map(float, n_input.split()))
result = sum_of_list(n_list)
print(f"Сумма всех чисел в списке: {result}")