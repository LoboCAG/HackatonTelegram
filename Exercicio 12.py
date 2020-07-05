alfabeto = "abcdefghijklmnopqrstuvwxyz"
cifra = "defghijklmnopqrstuvwxyzabc"
while True:
    choice = None
    codigo = ''
    msg = ''
    print("Escolha [C]odificar ou [D]ecifrar ou [0] para encerrar:")
    try:
        choice = input()
    except ValueError:
        print("Ops, Algo errado aconteceu, comece novamente:")
        continue
    if choice == '0':
        exit(0)
    else:
        pass
    print("Escreva a mensagem ou digite 0 para encerar:")
    try:
        msg = input()
    except ValueError:
        print("Ops, Algo errado aconteceu, comece novamente:")
        continue
    if choice.upper() == 'C':
        for i, letra in enumerate(msg):
            j = 0
            while msg[i] != alfabeto[j]:
                j += 1
            codigo += cifra[j]
    elif choice.upper() == 'D':
        for i, letra in enumerate(msg):
            j = 0
            while msg [i] != cifra[j]:
                j += 1
            codigo += alfabeto[j]
    else:
        print("Opção invalida, comece novamente:")
        continue
    print(codigo)