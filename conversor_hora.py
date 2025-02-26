# Kainan Fernando dia 17/05
##conversao de horas 12/24
def conversor_0(
    horas, minutos
):  # converte de 12 para 24 com o zero nos minutos menores que 10
    print("""=========""")
    print(f"|{horas:>3}:0{minutos:<2}|")
    print("""=========""")
    input("Digite enter para continuar")


def conversor_24(horas, minutos):  # converte de 12 para 24
    print("""=========""")
    print(f"|{horas:>3}:{minutos:<3}|")
    print("""=========""")
    input("Digite enter para continuar")


def conversao_120(
    horas, minutos
):  # converte de 24 para 12 com o zero nos minutos menores que 10
    print("""============""")
    if horas <= 12:
        print(f"|{horas:>3}:0{minutos:<2}A.M|")
    else:
        print(f"|{horas:>3}:0{minutos:<2}P.M|")
    print("""============""")
    input("Digite enter para continuar")


def conversao_12(horas, minutos):  # converte de 24 para 12
    print("""===========""")
    if horas <= 12:
        print(f"|{horas:>3}:{minutos:<2}A.M|")
    elif horas > 12:
        print(f"|{horas:>3}:{minutos:<2}P.M|")
    print("""===========""")
    input("Digite enter para continuar")


tabela = """================================================================================
|   Digite [1] para usar o estilo de 12 horas e converter para 24 horas.       |
|   Digite [2] para usar o estilo de 24 horas e converter para 12 horas.       |
|   Digite [3] para finalizar o programa.                                      |
|   *Consideramos 24 como 0                                                    |
================================================================================
"""
import os

# def convesor_horas(horas,minutos):
while True:
    os.system("cls")
    notacao = input(tabela)
    # opçao 12 horas para 24
    if notacao == "1":
        horas = int(input("\nDigite a hora que deseja converter: "))
        while horas > 12:  # validaçao da hora
            horas = int(input("Digite uma hora que seja valida: "))
        minutos = int(input("\nDigite agora os minutos: "))
        while minutos > 59:  # validaçao dos minutos
            minutos = int(input("Digite um minuto valido: "))
        periodo = input("\nDigite 1 para A.M., digite 2 para P.M.: ")
        while not periodo == 1 or periodo == 2:
            if periodo == "1":
                if minutos < 10:  # estética
                    conversor_0(horas, minutos)
                    break
                else:
                    conversor_24(horas, minutos)
                    break
            elif periodo == "2":
                if horas != 12:
                    horas = horas + 12
                if minutos < 10:  # estética
                    conversor_0(horas, minutos)
                    break
                else:
                    conversor_24(horas, minutos)
                    break
            else:
                print("Digite um opção válida")
                periodo = input("Digite 1 para A.M., digite 2 para P.M.: ")
    # opcao 24 horas para 12
    elif notacao == "2":
        horas = int(input("\nDigite a hora que deseja converter: "))
        while horas > 23:  # validaçao da hora
            horas = int(input("Digite uma hora que seja valida: "))
        minutos = int(input("\nDigite agora os minutos: "))
        while minutos > 59:  # validaçao dos minutos
            minutos = int(input("Digite um minuto valido: "))
        if horas > 12:  # P.M.
            horas = horas - 12
            if minutos < 10:  # estética
                conversao_120(horas, minutos)
            elif horas == 12:
                if minutos < 10:  # estética
                    conversao_120(horas, minutos)
                else:
                    conversao_12(horas, minutos)
            else:
                conversao_12(horas, minutos)
        else:  # A.M.
            if minutos < 10:  # estética
                conversao_120(horas, minutos)
            else:
                conversao_12(horas, minutos)
    elif notacao == "3":
        break
    # validação da opcao
    else:
        print("Digite um opção válida")
        input("Digite enter para tentar de novo")
# print(horas,':',minutos)
print("Obrigado por usar o programa :)")
