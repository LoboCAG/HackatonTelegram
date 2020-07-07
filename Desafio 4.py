# Validar CPF
print("Digite o CPF a ser testado:")
cpf = input();
cpf.replace(".", "")
cpf.replace("-", "")
# Testa se todos os digitos sao iguais, caso sim, retorna invalido
if cpf == '11111111111' or cpf == "22222222222" or cpf == "33333333333" or cpf == "44444444444" or cpf == "55555555555" or cpf == "66666666666" or cpf == "77777777777" or cpf == "88888888888" or cpf == "99999999999" or cpf == "00000000000":
    print("CPF inválido! Todos os digitos são iguais!")
elif len(cpf) != 11:
    print("CPF inválido, não possui 11 digitos!")
else:
    soma = 0
    peso = 10
    teste = cpf[:9]
    for i, letra in enumerate(teste):
        soma += (int(teste[i]) * peso)
        peso -= 1
    soma = soma % 11
    if soma > 1:
        soma = 11 - soma
    else:
        soma = 0
    teste = teste + (str(soma))
    peso = 11
    soma = 0
    for i, letra in enumerate(teste):
        soma += (int(teste[i]) * peso)
        peso -= 1
    soma = soma % 11
    if soma > 1:
        soma = 11 - soma
    else:
        soma = 0
    teste = teste + (str(soma))

    if cpf == teste:
        cpf = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]
        print("O CPF " + cpf + " é valido!")
    else:
        cpf = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]
        print("O CPF " + cpf + " é invalido")