from random import *

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100

def game_guess_the_number():
    count = 0
    print('Введите число n - правая граница для случайного выбора числа (от 1 до n)')
    num = int(input())
    number = randint(1, num)
    while True:
        print(f'Введите целое число от 1 до {num}')
        n = input()
        if is_valid(n) == False:
            print(f'А может быть все-таки введем целое число от 1 до {num}?')
            continue
        else:
            n = int(n)
            
        if n > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
            continue
        elif n < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
            continue
        elif n == number:
            count += 1
            print(f'Вы угадали число с {count}, раза! Поздравляем! :)\nХотели бы вы сыграть еще раз? Напшите да или нет')
            if input().lower() == 'да':
                game_guess_the_number()
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

print('Добро пожаловать в числовую угадайку')
game_guess_the_number()