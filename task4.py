# P.s. вывод в программе использован для наглядности
# Первый способ: с помощью перевода числа в строку и ее обработки

num = 578

def EvaluatorWithString(number):
    s = str(number) # перевод

    sum = 0 # переменная для суммы
    prod = 1 # переменная для произведения
    i = 0 # переменная для индекса

    while i < len(s):
        sum += int(s[i])
        prod *= int(s[i])
        i += 1

    return(sum, prod)

print(EvaluatorWithString(num))

# Второй способ: с помощью остатка от деления на 10

def EvaluatorWithExcess(number):
    sum = 0 # переменная для суммы
    prod = 1 # переменная для произведения

    while number != 0:
        sum += number % 10 # прибавляем по одной цифре
        prod *= number % 10  # умножаем на одну цифру
        number = number // 10 # отсекаем последнюю цифру

    return(sum, prod)

print(EvaluatorWithExcess(num))
