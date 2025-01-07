# Calculadora simples

print("--- Bem vindo a calculadora ---")

Calculadora_On = True

while Calculadora_On == True:
    print("--- Opçoes            ---"
          "\n--- 1 - soma          ---"
          "\n--- 2 - diminuiçao    ---"
          "\n--- 3 - multiplicaçao ---"
          "\n--- 4 - divisao       ---"
          "\n--- 5 - porcentagem   ---"
          "\n--- 6 - saida         ---")
    escolha = int(input("Qual opçao voce deseja calcular? "))
    if escolha == 1:
        numero1 = float(input("Digite um numero: "))
        numero2 = float(input("Digite outro numero: "))
        soma = numero1 + numero2
        print(soma)
    if escolha == 2:
        numero1 = float(input("Digite um numero: "))
        numero2 = float(input("Digite outro numero: "))
        diminuicao = numero1 - numero2
        print(diminuicao)
    if escolha == 3:
        numero1 = float(input("Digite um numero: "))
        numero2 = float(input("Digite outro numero: "))
        multiplicacao = numero1 * numero2
        print(multiplicacao)
    if escolha == 4:
        numero1 = float(input("Digite um numero: "))
        numero2 = float(input("Digite outro numero: "))
        divisao = numero1 / numero2
        print(divisao)
    if escolha == 5:
        numero1 = float(input("Digite um numero: "))
        numero2 = float(input("Digite a porcentagem: "))
        porcentagem = numero1 * (numero2 / 100)
        print(porcentagem)
    if escolha == 6:
        Calculadora_On = False
        print("Obrigado por usar!")
