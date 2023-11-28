import sys

if len(sys.argv) == 3:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():

        first_number: int = int(sys.argv[1])
        second_number: int = int(sys.argv[2])

        print(f'A soma do primeiro número com o segundo número é: {first_number + second_number}')

    else:
        print('Os valores precisam ser numéricos!')

else:
    print('É preciso dois números como argumento!')