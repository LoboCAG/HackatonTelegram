alfabeto = "abcdefghijklmnopqrstuvwxyz1234567890"
morse = ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", "-....", "--...", "---..", "----.", "-----"
while True:
    codigo = ""
    print("Escolha [C]odificar ou [0] Sair")
    operacao = input()
    if operacao.upper() == "C":
        print("Escreva a mensagem:")
        msg = input()
        for i, letra in enumerate(msg):
            ind = 0
            tmp = msg[i]
            while tmp != alfabeto[ind]:
                ind += 1
            codigo += morse[ind]
        print(codigo)
    elif operacao == "0":
        exit(0)
    else:
        print("Opção invalida")
        continue