print("Digite F para Converter para Farenheint ou C para Celsius e X oara encerrar")
tipo = input()
while True:
    temp = int(0)
    if tipo == 'F' or tipo == 'f':
        print("Digite a temperatura em Celsius")
        temp = int(input())
        temp= (temp - 32) * 5/9
        print("%s ºF" % temp)
    elif tipo == 'C' or tipo == 'c':
        print("Digite a temperatura em Farenheint")
        temp = int(input())
        print((temp*9/5)+32, "ºC")
    elif tipo == 'X' or tipo == 'x':
        exit(0)
    else:
        print("Opção invalida")
    print("Digite F para Converter para Farenheint ou C para Celsius e X oara encerrar")
    tipo = input()