def custom_filter(some_list):
    result = 0
    for i in some_list:
        if (isinstance(i, int)) and (i % 7 == 0):
            result += i
    if result <= 83:
        return True
    else:
        return False


anonymous_filter = lambda s: sum(1 for char in s if char.lower() == 'я') >= 23

# Пример использования:
print(anonymous_filter("я " * 23))  # Вывод: True
print(anonymous_filter("Пример строки с буквой я."))  # Вывод: False