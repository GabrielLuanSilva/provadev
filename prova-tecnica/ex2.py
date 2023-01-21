def less_then(num: int):
    return num < 10


def is_even(num: int):
    return num % 2 == 0


def between(num: int):
    return 8 <= num <= 16  # num >= 8 and num <= 16


def equals(num: int):
    return num == 51 or num == 80


if __name__ == '__main__':
    entrada: int = int(input())

    if less_then(entrada):
        print('O número é menor que 10')
    if is_even(entrada):
        print('O número é par.')
    if between(entrada):
        print('O número está entre 8 e 16.')
    if equals(entrada):
        print('O número é 51 ou 80.')
