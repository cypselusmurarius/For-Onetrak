# P.s. вывод в программе использован для наглядности

hw = "Hello World"

# Первый способ: с помощью срезов(просто, элегантно, быстро)

def UpAndReverseWithSlice(str):
    str = str[::-1] # реверс строки
    str = str.upper() # перевод букв в верхний регистр

    return str

print(UpAndReverseWithSlice(hw))

# Назначаем значение по умолчанию

hw = "Hello World"

# Второй способ: проход с помощью цикла по строке

def UpAndReverseWithLoop(str):
    s1 = "" # ввод вспомогательной локальной переменной
    n = len(str) - 1 # нахождение последнего индекса строки

    # пока строка не закончилась
    while n >= 0:
        s1 += str[n] # конкатенация строк
        n -= 1 # уменьшение индекса

    str = s1
    str = str.upper() # перевод букв в верхний регистр

    return str

print(UpAndReverseWithLoop(hw))

# Назначаем значение по умолчанию

hw = "Hello World"

# Третий способ: с помощью методов join и reversed

def UpAndReverseWithJoin(str):
    str = ''.join(reversed(str))
    str = str.upper() # перевод букв в верхний регистр

    return str

print(UpAndReverseWithJoin(hw))
