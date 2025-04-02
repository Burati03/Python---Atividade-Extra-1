import random

def contador_de_tentativas():
    numero_gerado = random.randint(1, 100)
    tentativa = None
    tentativas = 0

    while tentativa != numero_gerado:
        tentativa = int(input("Escolha um número de 1 a 100: "))
        tentativas += 1
        
        if tentativa < numero_gerado:
            print("O número é maior. Tente novamente.")
        elif tentativa > numero_gerado:
            print("O número é menor. Tente novamente.")
        else:
            print(f"Parabéns, você acertou! O número era {numero_gerado}. Você tentou {tentativas} vezes.")

contador_de_tentativas()