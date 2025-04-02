import random 

def contador_de_tentativas():
 
tentativa = None

numero_gerado = random.uniform(1,100)

while tentativa != numero_gerado: 
    tentativa = int(input("Escolha um número de 1 a 100 "))

if numero True
    print(f"Parabéns você acertou o numero! O número é {numero_gerado} ")

else numero False 
    print("Você errou, tente novamente")

contador_de_tentativas()