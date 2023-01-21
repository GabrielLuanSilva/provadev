def string_concat(*args) -> str:
    return ','.join(args) if len(args) != 0 else ''


def main() -> None:
    var1 = input('Insira entrada 1: ')
    var2 = input('Insira entrada 2: ')
    print(string_concat(var1, var2))


if __name__ == '__main__':
    main()
