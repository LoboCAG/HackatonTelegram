import random
player_pts = 0 #pontos do jogador
pc_pts = 0 #pontos do Computador
player = 0
print("Por favor, escolha uma opção:")
while True:
    pc = 0
    opcoes = ["Pedra", "Tesoura", "Papel"]
    print("[0] Pedra\n[1] Tesoura\n[2] Papel\n[3] Sair")
    try:
        player = int(input())
    except ValueError:
        print("Opção invalida, por favor escolha novamente:")
        continue
    if player < 0 or player > 3:  #Escolha do jogador deve ser entre 0 e 3
        print("opção invalida, por favor escolha novamente:")
        continue
    elif player == 3: #opção 3 encerra o jogo
        print("Placar: \nJogador: " + str(player_pts) +"\nOponente: " + str(pc_pts) + "\nObrigado! E venha jogar novamente! :D")
        exit(0)
    else:  #computador sorteia a opção
        pc = random.randint(0,2)
        print(opcoes[player] + " " + opcoes[pc])
    #Opções com vitoria do jogador
    if player == 0 and pc ==1:
        player_pts += 1
        print("Voce escolheu " + opcoes[player] + ", seu oponente escolheu " + str(opcoes[pc]) + ". Você venceu!")
        print("Placar: \nJogador: " + str(player_pts) +"\nOponente: " + str(pc_pts))
        print("Escolha novamente:")
    elif player == 1 and pc == 2:
        player_pts += 1
        print("Voce escolheu " + opcoes[player] + ", seu oponente escolheu " + str(opcoes[pc]) + ". Você venceu!")
        print("Placar: \nJogador: " + str(player_pts) +"\nOponente: " + str(pc_pts))
        print("Escolha novamente:")
    elif player == 2 and pc == 0:
        player_pts += 1
        print("Voce escolheu " + opcoes[player] + ", seu oponente escolheu " + str(opcoes[pc]) + ". Você venceu!")
        print("Placar: \nJogador: " + str(player_pts) +"\nOponente: " + str(pc_pts))
        print("Escolha novamente:")
    elif player == pc: #Empate entre computador e jogador
        print("Você e seu oponente escolheram " + opcoes[player] + ". Vocês empataram, ninguem ganha ponto!")
        print("Escolha novamente:")
    #Opções com vitoria do computador
    else:
        pc_pts += 1
        print("Voce escolheu " + opcoes[player] + ", seu oponente escolheu " + str(opcoes[pc]) + ". Você perdeu!")
        print("Placar: \nJogador: " + str(player_pts) +"\nOponente: " + str(pc_pts))
        print("Escolha novamente:")