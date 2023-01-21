"""1. Faça um laço de repetição que comece a contar a partir do número 1 e que vá
incrementando de 2 em 2 até chegar no número 9. Exemplo de saída que este
sistema irá gerar quando executá-lo:"""


def print_numbers():
    for n in range(1, 10, 2):
        print(n, end=' ')


if __name__ == '__main__':
    print_numbers()
