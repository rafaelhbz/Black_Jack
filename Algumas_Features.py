# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:30:37 2019

@author: RafaelzZ
"""
#------------------------------ Feature 1 ----------------------------------  

jogo_comeca = False

dinheiro_do_jogador = int(input('Quanto dinheiro vc tem disponivel para o jogo ? '))
while dinheiro_do_jogador < 0 or dinheiro_do_jogador == 0:
    dinheiro_do_jogador = int(input('Quanto dinheiro vc tem disponivel para o jogo ? '))
    
    
aposta = int(input('Quanto dinheiro você quer apostar ? '))
while aposta < 0 or aposta == 0:
    aposta = int(input('Quanto dinheiro você quer apostar ? '))

if aposta > dinheiro_do_jogador:
    print('Sr.,vá dar golpe na sua mãe!! ')
elif aposta ==0:
    print('Tente um valor maior do que zero')
elif dinheiro_do_jogador < 0:
    print('Tente um valor maior do que zero')
elif aposta < 0:
    print('Qual é o seu problema ?')
else:
    jogo_comeca = True


if jogo_comeca == True:
    print('O jogo começou')
    


#------------------------------ Feature 5 ----------------------------------  
    


if jogo_comeca == True:
    numero_baralhos = int(input('Digite o numero de baralhos que serão utilizados: '))

baralho = { "Ás" : 4, "Dois" : 4, "Três" : 4, "Quatro" : 4, "Cinco" : 4, "Seis" : 4, "Sete" : 4, "Oito" : 4, "Nove" : 4,
           "Dez" : 4, "Valete" : 4, "Dama" : 4, "Rei" : 4 }


cartas = []
numero = []

for key in baralho.keys():
    cartas.append(key)
    
for values in baralho.values():
    numero.append(values)
    

baralho_novo = {}

i = 0
while i < len(cartas):
    baralho_novo[cartas[i]] = 4 * numero_baralhos
    i+=1
    
print(baralho_novo)




#------------------------------ Feature 6 ----------------------------------  




print('                                         *          ')
print('                                       *   *        ')
print(' *       *    * * * *     * * * *     * * * *       ')
print('  *     *     *     *     *           *             ')
print('   *   *      *     *     *           * * * *       '  )
print('    * *       *     *     *           *              ')
print('     *        * * * *     * * * *     * * * *          ' )
print('')
print('')
print('  * * * *     * * * *      * * * *    * * *     * * * *   *     *          ')
print('  *     *     *            *     *    *     *   *         *     *      ')
print('  * * * *     * * * *      * * * *    *     *   * * * *   *     *         ')
print('  *           *            * *        *     *   *         *     *   ')
print('  *           * * * *      *   *      * * *     * * * *   * * * *     ')
print('')
print('')
print(' *   .        * * * * * * * *                            ')
print('  *  *     *                  *      \                       ')
print('* .  * *   *     *      *     *     -- **********/             ')
print('  * . * ** *   * * *  * * *   *     -- ************             ')
print('*  . * *   *     *      *     *      /          ****            ')
print('  . *      *                  *                  ****             ')
print('*  .       *       *****      *                          ')
print('  *        *       *   *      *              ')
print(' * * .     *        ***       *             ')
print('  *         * * * * * * * * *                ')










