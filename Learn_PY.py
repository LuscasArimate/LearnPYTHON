
# Tabuada

'''
num = int(input('Digite um número pra ver a tabuada:'))

print ('-' *12) 

print ('{} x {} = {}'.format(num,1,num*1))
print ('{} x {} = {}'.format(num,2,num*2))
print ('{} x {} = {}'.format(num,3,num*3))
print ('{} x {} = {}'.format(num,4,num*4))
print ('{} x {} = {}'.format(num,5,num*5))
print ('{} x {} = {}'.format(num,6,num*6))
print ('{} x {} = {}'.format(num,7,num*7))
print ('{} x {} = {}'.format(num,8,num*8))
print ('{} x {} = {}'.format(num,9,num*9))
print ('{} x {} = {}'.format(num,10,num*10))

print('-' *12)

'''


# Calculando raiz quadrada de um numero

'''
import math 
num= int(input('digite um numero, cria :'))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {:.2f}'.format(num,raiz))
		
'''

#Calculando desconto

'''


preço = float(input('Qual o preço do produto? R$'))
desc = float(input('Qual o valor do seu desconto? %'))
novo = preço - (preço * desc/100)
print('O produto que custava R${}, com o desconto de {}% agora custa {}'.format(preço,desc,novo))


'''

#Reproduzir.mp3

'''

import pygame 
pygame.init()
pygame.mixer.music.load('CAFE.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''


# Sistema de ajuda(help) Python 


''''

ta travado no meu celular, dps termino 
python ep 106 exercicios curso em video


def ajuda(com):
    help(com)
    
    
## Main
 
comando= ''
while True:
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == 'FIM' or 'END' :
        break
    else:
        ajuda(comando)
        
'''



#Primeiro condicional 

'''
resposta = str(input('Você me ama? s/n '))

while resposta not in 'SsSimsim':
    resposta = str(input('Resposta invalida, por favor corrija  '))
print('Sefoda mlk kkkk, trouxa')
print('Quitei')

'''


#Contagem regressiva

'''

from time import sleep

num=int(input('Informe de qual numero irá começar a contagem! '))


for cont in range(num,0,-1):
    print (cont)
    sleep(0.9)
sleep(0.6)
print('gozei')

'''

#A classica da media

'''

n1= int(input('Digite a nota 1 '))
n2= int(input('Digite a nota 2 '))
n3= int(input('Digite a nota 3 '))
s= (n1 + n2 + n3)
m= s/3
print('Sua media é ',m)


'''

#Entendendo Array


'''

frutas = []

# Solicitar frutas favoritas
while True:
    fruta = str(input("Digite uma fruta favorita (ou 'sair' para encerrar): "))
    if fruta.lower() == "sair":
        break
    frutas.append(fruta)

# Exibir as frutas favoritas
print("Suas frutas favoritas são: ")
for fruta in frutas:
    print(fruta)
    

'''

#Analisador de triângulos 

'''
import math 


print("-="*18)
print("Analisador de Triângulos" )
print("-="*18)



resposta = str(input('É um triângulo retângulo? s/n '))

while resposta not in 'SsSimsim':
    
    r1 = float(input("\n Primeiro segmento "))
    r2 = float(input(" Segundo segmento "))
    r3 = float(input(" Terceito segmento "))

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
     print("")
     print("\n Os segmentos acima podem formar um triângulo")

    else:
     print("\n Os segmentos acima nao podem formar um triângulo")


    if r1 == r2 == r3:
    
     print("\n Esse triângulo é EQUILATERO")
     peri=(float(r1 + r2 + r3))
     print ("e seu perimetro é de {} u.m".format(peri))
    
    
    elif r1 == r2 or r2 == r3 or r1 == r3:
     print("\n Esse triângulo é ISOCELES")
     peri=(float(r1 + r2 + r3))
     print ("e seu perimetro é de {} u.m".format(peri))
    
    
    else:
     print("\n Esse triângulo é ESCALENO")
     peri=(float(r1 + r2 + r3))
     print ("e seu perimetro é de {} u.m".format(peri))
     
     break
    



c1 = float(input("\n Primeiro cateto "))
c2 = float(input(" Segundo cateto "))




def calcular_hipotenusa(c1, c2):
    hipotenusa = math.sqrt(c1**2 + c2**2)
    return hipotenusa


resultado = calcular_hipotenusa(c1, c2)
print("\n Hipotenusa= : resultado {:.2f}".format(resultado))


'''


'''

#Rolagem de Dados

import random

def roll_dice(dice_notation):
    num_dice, num_sides = dice_notation.split('d')
    num_dice = int(num_dice)
    num_sides = int(num_sides)

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

def main():
    dice_notation = input("Insira a notação do dado(e.g., 1d20, 2d6): ")
    rolls = roll_dice(dice_notation)
    print("Dados rolados:", rolls)
    print("Total:", sum(rolls))

if __name__ == '__main__':
    main()
    
'''


