a = int(input('ПЕРВОЕ '))
b = int(input('ВТОРОЕ '))
c = int(input('ТРЕТЬЕ '))

def int_input(message):
    while True:
        try:
            result = int(input(message)
            a = int(input())
            b = int(input('ВТОРОЕ '))
            c = int(input('ТРЕТЬЕ '))
        except ValueError:
            print('Вы ввели не то число')
        except Exception as error:
            print(f'НЕИЗВЕСТНАЯ ОШИБКА: {type(error)} {error}')
        else:
            return result