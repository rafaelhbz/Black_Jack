# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:41:27 2019

@author: RafaelzZ
"""
print("-----<@")
print("BOM JOGO")
print("@>------")

jogadores = []
dinheiro_jogadores = []

tem_mais_jogadores = str(input("Existem mais jogadores? Digite sim ou não "))
while tem_mais_jogadores == "sim" or tem_mais_jogadores == "Sim":
    jogador_adicionado = str(input("Digite o seu nome, nobre jogador "))
    dinheiro_começo = int(input("Com quanto dinheiro você deseja começar ?"))
    jogadores.append(jogador_adicionado)
    dinheiro_jogadores.append(dinheiro_começo)
    tem_mais_jogadores = str(input(" Se houver mais jogadores, por favor responda que sim"))
    
padrao_jogo = {}
i = 0
while i < len(jogadores):
    padrao_jogo[jogadores[i]] = dinheiro_jogadores[i]   
    i = i + 1
print(padrao_jogo)
game_init = True
while game_init == True:
    
    deletados = []
    
    for i in padrao_jogo.keys():
        if padrao_jogo[i] == 0:
            deletados.append(i)
            
    print(deletados)
#    
    pontuação_dealer = 0
    
    import random
    
    baralho = { "1" : 4, "2" : 4, "3" : 4, "4" : 4, "5" : 4, "6" : 4, "7" : 4, "8" : 4, "9" : 4,
               "10" : 4, "Valete" : 4, "Dama" : 4, "Rei" : 4 }
    
    numero_baralhos = int(input("Digite quantos baralhos serão utilizados: "))
    
    numero_cartas = []
    
    cartas_baralho = []
    
    for cartas in baralho.keys():
        cartas_baralho.append(cartas)
    
    for valores in baralho.values():
        numero_cartas.append(valores * numero_baralhos)
        
    embaralha = random.shuffle(cartas_baralho)
    
    #print(cartas_baralho)
    #print(numero_cartas)
    
    
    baralho_modificado = {}
    
    i = 0
    while i < len(numero_cartas):
        for keys in cartas_baralho:
            baralho_modificado[keys] = numero_cartas[i]
        i = i + 1
        
    #print(baralho_modificado)
    
    #print(str(random.choice(list(baralho_modificado.keys()))))
    
    
    def retira_cartas(baralho_modificado, jogador):
        
        valores_dez = ["Dez","Valete", "Dama", "Rei"]
        global pontuação_jogador
        pontuação_jogador = 0
        
        primeira_jogada = 0
        while primeira_jogada < 2:
            sorteio_local = str(random.choice(list(baralho_modificado.keys())))
            print("A carta sorteada foi {}".format(sorteio_local))
            baralho_modificado[sorteio_local] = baralho_modificado[sorteio_local] - 1
            if sorteio_local in valores_dez:
                pontuação_jogador = pontuação_jogador + 10
            elif sorteio_local == "Ás":
                if pontuação_jogador < 11:
                    pontuação_jogador = pontuação_jogador + 11
                else:
                    pontuação_jogador = pontuação_jogador + 1
            else:
                pontuação_jogador = pontuação_jogador + int(sorteio_local)
            primeira_jogada = primeira_jogada + 1
        print(pontuação_jogador)
        desejo = str(input("{0}, você quer tirar mais uma carta? ".format(jogador)))
        while desejo == "Sim" or desejo == "sim":
            sorteio_local = str(random.choice(list(baralho_modificado.keys())))
            print("A carta sorteada foi {}".format(sorteio_local))
            baralho_modificado[sorteio_local] = baralho_modificado[sorteio_local] - 1
            if sorteio_local in valores_dez:
                pontuação_jogador = pontuação_jogador + 10
            elif sorteio_local == "Ás":
                if pontuação_jogador < 11:
                    pontuação_jogador = pontuação_jogador + 11
                else:
                    pontuação_jogador = pontuação_jogador + 1
            else:
                pontuação_jogador = pontuação_jogador + int(sorteio_local)
            print("{0} a sua pontuação agora é {1}".format(jogador,pontuação_jogador))
            
            if pontuação_jogador >= 21:
                break
            else:
                desejo = str(input("{0} quer continuar retirando cartas? ".format(jogador)))
        print(pontuação_jogador)
        return baralho_modificado, pontuação_jogador
    
    #retira_cartas(baralho_modificados
    
    #for i in jogadores:
    #    pontuação.append(retira_cartas(baralho_modificado)[1])
        
    #print(baralho_modificado)
    
    pontuação_dealer = 0
    
    def coupier_retirando(baralho_modificado):
        
        valores_dez = ["Dez","Valete", "Dama", "Rei"]
        
        global pontuação_dealer
        pontuação_dealer = 0
        
        primeira_jogada = 0
        while primeira_jogada < 2:
            sorteio_local = str(random.choice(list(baralho_modificado.keys())))
            print("A carta sorteada foi {0}".format(sorteio_local))
            baralho_modificado[sorteio_local] = baralho_modificado[sorteio_local] - 1
            if sorteio_local in valores_dez:
                pontuação_dealer = pontuação_dealer + 10
    #            print(pontuação_dealer)
            elif sorteio_local == "Ás":
                if pontuação_dealer < 11:
                    pontuação_dealer = pontuação_dealer + 11
                else:
                    pontuação_dealer = pontuação_dealer + 1
            else:
                pontuação_dealer = pontuação_dealer + int(sorteio_local)
    #            print(pontuação_dealer)
            primeira_jogada = primeira_jogada + 1
            
        while pontuação_dealer < 17:
            sorteio_local = str(random.choice(list(baralho_modificado.keys())))
            print("A carta sorteada foi {0}".format(sorteio_local))
            baralho_modificado[sorteio_local] = baralho_modificado[sorteio_local] - 1
            if sorteio_local in valores_dez:
                pontuação_dealer = pontuação_dealer + 10
            elif sorteio_local == "Ás":
                if pontuação_dealer < 11:
                    pontuação_dealer = pontuação_dealer + 11
                else:
                    pontuação_dealer = pontuação_dealer + 1
            else:
                pontuação_dealer = pontuação_dealer + float(sorteio_local)
        return baralho_modificado, pontuação_dealer
    
    pontuação_jogadores = []
    jogadores_limpinhos = []
    index = 0
    while index < len(jogadores):
        if jogadores[index] not in deletados:
            jogadores_limpinhos.append(jogadores[index])
        index = index + 1
            
    print(jogadores_limpinhos)
        
    for i in jogadores_limpinhos:
        print("{0} quanto você deseja apostar? ".format(i))
        apostar = int(input("Digite o valor da sua aposta "))
        while apostar < 0 or apostar > padrao_jogo[i]:
            apostar = int(input("Seu corno, seja homi e aposta o que tenha: " ))
        pontuação_jogadores.append(retira_cartas(baralho_modificado, i)[1])
    
    print(jogadores)
    print(pontuação_jogadores)
            
    placar = {}
    contador = 0
    while contador < len(pontuação_jogadores):
        placar[jogadores_limpinhos[contador]] = pontuação_jogadores[contador]
        contador = contador + 1
    print(placar)
    
    coupier_retirando(baralho_modificado)
    print(pontuação_dealer)
    
    contador_dois = 0
    chaves_dicionario = list(placar.keys())
    valor_dicionario_dinherio = list(padrao_jogo.values())
    while contador_dois < len(chaves_dicionario):
        if placar[chaves_dicionario[contador_dois]] == 21:
            padrao_jogo[jogadores_limpinhos[contador_dois]] = padrao_jogo[jogadores_limpinhos[contador_dois]] + 2.5 * apostar
            
        elif placar[chaves_dicionario[contador_dois]] > pontuação_dealer and placar[chaves_dicionario[contador_dois]] < 21:
            padrao_jogo[jogadores_limpinhos[contador_dois]] = 2 * padrao_jogo[jogadores_limpinhos[contador_dois]] + 2 * apostar
            
        elif padrao_jogo[jogadores_limpinhos[contador_dois]] == pontuação_dealer:
            padrao_jogo[jogadores_limpinhos[contador_dois]] = padrao_jogo[jogadores_limpinhos[contador_dois]]
            
        elif placar[chaves_dicionario[contador_dois]] < 21 and pontuação_dealer > 21:
            placar[chaves_dicionario[contador_dois]] = 2 * placar[chaves_dicionario[contador_dois]]
            
        else:
            padrao_jogo[jogadores_limpinhos[contador_dois]] = padrao_jogo[jogadores_limpinhos[contador_dois]] - apostar
            
        contador_dois = contador_dois + 1
    
    print(padrao_jogo)
    
    if len(jogadores_limpinhos
           ) == 0:
        break
#    print(deletados)
    print("******************************************************************")
    print("Se quiser parar de jogar digite fim")
    print("******************************************************************")
    quer_jogar = str(input("Deseja continuar jogando? "))
    if quer_jogar == "Fim" or quer_jogar == "fim":
        game_init = False