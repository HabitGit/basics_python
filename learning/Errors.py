# x = 0
# while x == 0:
#     try:
#         x = int(input('Введите число: '))
#         x += 5
#         print(x)
#     except ValueError:
#         print('Введите именно число')

try:
    x = 5 / 0
    x = int(input())
except ZeroDivisionError:
    print('Деление на ноль!')
except ValueError:
    print('Вы ввели что-то не так')
else:
    print('Else')
finally:
    print('Finally')