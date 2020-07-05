num_rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
num_arab = [1, 5, 10, 50, 100, 500, 1000]
tmp1 = '0'
tmp2 = '0'
while True:
    total = 0
    print("Digite um número em algarismo romano")
    romano = None
    romano = (input())
    romano = romano.upper()
    j = -1
    for i, letra in enumerate(romano):
        j += 1
        tmp1 = romano[j]
        if j < len(romano)-1:
            tmp2 = romano[j+1]
        tmp3 = 0
        try:
            while tmp1 != num_rom[tmp3]:
                tmp3 += 1
            tmp1 = num_arab[tmp3]
            tmp3 = 0
        except:
            print("Não é um algarismo romano!")
            break
        if j < len(romano)-1:
            if tmp2 != '0':
                while tmp2 != num_rom[tmp3]:
                    tmp3 += 1
                tmp2 = num_arab[tmp3]
            if int(tmp1) >= int(tmp2):
                total = int(total) + int(tmp1)
                if j >= len(romano)-1:
                    break
            else:
                total = int(total + tmp2 - tmp1)
                j +=1
                if j >= len(romano)-1:
                    break
        else:
            total = int(total) + int(tmp1)
            break
    if total == 0:
        pass
    else:
        print("Você digitou " + romano + " que equivale a " + str(total))
    while True:
        print("Deseja converter outro numero? S/N")
        conf = input()
        if conf.upper() == 'N':
            exit(0)
        elif conf.upper() == 'S':
            break
        else:
            print("Opção invalida!")