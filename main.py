import math
import os

def menu():  
    #2 pontos é igual ao {} em C
    print("Escolha o tipo de função para calcular a derivada:")
    print("0. Fechar programa")
    print("1. 1. Simples f(x) = ax")
    print("2. Regra da potência f(x) = ax^n")
    print("3. Regra de raiz quadrada f(x) = √(ax)")
    print("4. Logaritmo f(x) = log(a)")
    print("5. Ln f(x) = ln(a)")
    print("6. Exponencial f(x) = a^x")
    print("7. Exponencial com Euler f(x) = e^ax")
    print("8. Seno f(x) = sin(ax)")
    print("9. Cosseno f(x) = cos(ax)")
    print("10. Tangente f(x) = tg(ax)")
    print("11. Cotangente f(x) = ctg(ax)")
    print("12. Secante f(x) = sec(ax)")
    print("13. Cossecante f(x) = csc(ax)")
    print("14. Polinômio (ax^n + bx + c)")
    print("15. Seno sin(ax + b)")
    print("16. Euler e^(ax + b)")
    

    #Função que calcula a derivada de f(x) = ax
def derivada_x(a, tem_variavel):
    if tem_variavel:
        print(f"A derivada de f(x) = {a}x") #tem que ter f antes dos "" para associar {a} se não imprime
        print(f"f'(x) = {a}")
    else:
        print(f"A derivada de f(x) = {a}")
        print("f'(x) = 0")
        
    #Função que calcula a derivada de f(x) = ax^n

def derivada_com_expoente(a, n):
    aa = a * n;
    nn = n - 1;
    print(f"A derivada de f(x) = {a}x^{n}")
    if nn == 1:
        print(f"f'(x) = {aa}x")
    elif nn == 0:
        print(f"f'(x) = {aa}");
    elif nn + 1 == 0:
        print("f'(x) = 0");
    else:
        print(f"f'(x) = {aa}x^{nn}")
        
    aaa = aa * nn;
    nnn = nn - 1;
    if nnn == 1: 
        print(f"f''(x) = {aaa}x")
    elif nnn == 0:
        print(f"f''(x) = {aaa}")
    elif nnn + 2 == 0 or nnn == -1: 
        print("f''(x) = 0")
    else:
        print(f"f''(x) = {aaa}x^{nnn}")
    
    
    #Função que calcula a derivada de f(x) = √ax
def derivada_raiz(a, tem_variavel):
    numerador = 1
    if tem_variavel:
        print(f"A derivada de f(x) = √{a}x")
        print(f"f'(x) = 1 / (2√{a}) * {a}")
        ehDivisivel = a % 2 == 0
        if ehDivisivel:
            numerador = a / 2
            print(f"f'(x) = {numerador} / √{a}x")
        else:
            numerador *= a
            print(f"f'(x) = {numerador} / 2√{a}x")
            
    else:
        print(f"f'(x) = 1 / (2√{a})")
        
    #Função que calcula a derivada de f(x) = log a
def derivada_log(a):
    print(f"A derivada de f(x) = log {a}")
    print(f"f'(x) = 1/({a} * ln 10)")
    
    #Função que calcula a derivada de f(x) = ln a
def derivada_ln(a):
    print(f"A derivada de f(x) = ln {a}")
    print(f"f'(x) = 1/{a}")
    
    #Função que calcula a derivada de f(x) = a^x
def derivada_exponencial(a):
    print(f"A derivada de f(x) = {a}^x")
    print(f"f'(x) = {a}^x * ln {a}")

    #Função que calcula a derivada de f(x) = e^x
def derivada_exponencial_euler(n, tem_variavel):
    if tem_variavel:
        print(f"A derivada de f(x) = e^{n}x")
        print(f"f'(x) = {n}e^{n}x")
    else:
        print(f"A derivada de f(x) = e^{n}")
        print("f'(x) = 0")

    #Função que calcula a derivada de f(x) = sen ax
def derivada_sin(a, tem_variavel):
    if tem_variavel:
        print(f"A derivada de f(x) = sen {a}x")
        print(f"f'(x) = {a}cos {abs(a)}x")
    else:
        print(f"A derivada de f(x) = sen {a}")
        print("f'(x) = 0")
        
    #Função que calcula a derivada de f(x) = cos ax
def derivada_cos(a, tem_variavel):
    if tem_variavel:
        print(f"A derivada de f(x) = cos {a}x")
        if a < 0:
            print(f"f'(x) = {a}sen {abs(a)}x")
        else:
            print(f"f'(x) = -{a}sen {a}x")
    else:
        print(f"A derivada de f(x) = cos {a}")
        print("f'(x) = 0")
        
    #Função que calcula a derivada de f(x) = tg ax
def derivada_tg(a, tem_variavel):
        if tem_variavel:
            print(f"A derivada de f(x) = tg {a}x")
            print(f"f'(x) = {a}sec^2 {abs(a)}x")
        else:
            print(f"A derivada de f(x) = {a}")
            print("f'(x) = 0")
        
    #Função que calcula a derivada de f(x) = ctg ax
def derivada_ctg(a, tem_variavel):
        if tem_variavel:
            print(f"A derivada de f(x) = ctg {a}x")
            print(f"f'(x) = {-a}csc^2 {abs(a)}x")
        else:
            print(f"A derivada de f(x) = ctg {a}")
            print("f'(x) = 0")
    
    #Função que calcula a derivada de f(x) = sec ax 
def derivada_sec(a, tem_variavel):
        if tem_variavel:
            print(f"A derivada de f(x) = sec {a}x")
            print(f"f'(x) = {abs(a)}(tg {abs(a)}x * sec{abs(a)}x)")
        else:
            print(f"A derivada de f(x) = sec {a}")
            print("f'(x) = 0")
    
    #Função que calcula a derivada de f(x) = csc ax
def derivada_csc(a, tem_variavel):
    if tem_variavel:
        print(f"A derivada de f(x) = csc {a}x")
        print(f"f'(x) = {-a}ctg {abs(a)}x * csc {abs(a)}x")
    else:
        print(f"A derivada de f(x) = csc {a}")
        print("f'(x) = 0")

    #Função que calcula a derivada de f(x) = ax^n + bx + c
def derivada_polinomio(a, n, b, c):
    da = a * n  
    dn = n - 1  
    db = b      

    print(f"A derivada de f(x) = {a}x^{n} + {b}x + {c}")
    print(f"f'(x) = {da}x^{dn} + {db}")

    
    #Função que calcula a derivada de f(x) = sin(ax + b)
def derivada_seno(a, b):
    print(f"A derivada de f(x) = sin({a}x + {b})")
    print(f"f'(x) = {a}cos({a}x)")

    #Função que exibe a derivada de f(x) = e^(ax + b)
def derivada_exp(a, b):
    print(f"A derivada de f(x) = e^({a}x + {b})")
    print(f"f'(x) = e^({a}x + {b}) . {a}")

    
    #Função que lê o valor de a em uma equação
def digite_valor_a():
    a = int(input("Digite o valor de a: "))
    print()
    return a

    #Função que diz por si só o que faz
def verifica_variavel():
    while True:
        resposta = input("Essa função vai ter variável? [S/N]: ").strip().upper() #input recebe a resposta, strip remove se o usurario botou espaço em branco, upper reebe maiusculo e menusculo
        if resposta in ('S'):
            return True
        elif resposta in ('N'):
            return False
            
        else:
            print("Resposta inválida!")
            return False



def main():
    
    continua = 'S'
    
    while continua == 'S':
    
        menu()
        escolha = int(input("Escolha uma das opções: "))
        
        match escolha:
            case 0:
                print()
                print("Programa fechado")
            
            case 1:
                a = digite_valor_a()
                tem_variavel = verifica_variavel()
                print()
                derivada_x(a, tem_variavel)
            
            case 2:
                a = digite_valor_a()
                n = int(input("Digite o valor de n: "))
                print()
                derivada_com_expoente(a, n)
            
            case 3:
                a = digite_valor_a()
                tem_variavel = verifica_variavel()
                print()
                derivada_raiz(a, tem_variavel)
                
            case 4:
                a = digite_valor_a()
                print()
                derivada_log(a)
                
            case 5:
                a = digite_valor_a()
                print()
                derivada_ln(a)
                
            case 6:
                a = digite_valor_a()
                print()
                derivada_exponencial(a)
                
            case 7:
                tem_variavel = verifica_variavel()
                n = int(input("Digite o valor de n: "))
                print()
                derivada_exponencial_euler(n, tem_variavel)
                
            case 8:
                a = digite_valor_a()
                tem_variavel = verifica_variavel()
                print()
                derivada_sin(a, tem_variavel)
                
            case 9:
                a = digite_valor_a()
                tem_variavel = verifica_variavel()
                print()
                derivada_cos(a, tem_variavel)
                
            case 10:
                a = digite_valor_a()
                tem_variavel = verifica_variavel()
                print()
                derivada_tg(a, tem_variavel)
                
            case 11:
                a = digite_valor_a()
                tem_variavel = verifica_variavel()
                print()
                derivada_ctg(a, tem_variavel)
                
            case 12:
                a = digite_valor_a()
                tem_variavel = verifica_variavel()
                print()
                derivada_sec(a, tem_variavel)
                
            case 13:
                a = digite_valor_a()
                tem_variavel = verifica_variavel()
                print()
                derivada_csc(a, tem_variavel)
                
            case 14:
                a = digite_valor_a()
                n = int(input("Digite o valor de n: "))
                b = int(input("Digite o valor de b: "))
                c = int(input("Digite o valor de c: "))
                print()
                derivada_polinomio(a, n, b, c)
                
            case 15:
                a = digite_valor_a()
                b = int(input("Digite o valor de b: "))
                print()
                derivada_seno(a, b)
                
            case 16:
                a = digite_valor_a()
                b = int(input("Digite o valor de b: "))
                print()
                derivada_exp(a, b)
                
            case _:
                print("Opção inválida!")
        
        continua = input("Deseja continuar?(S, N): ").strip().upper()
        if continua == 'S':
            os.system('cls' if os.name == 'nt' else 'clear')
        
        
    
    
if __name__ == "__main__":
    main()
    
