# Escolha dois números, em seguida sua operação matemática
from structure import *

primeiro_numero = float(input("Escolha o primeiro número: "))
segundo_numero = float(input("Escolha o segundo número: "))

while True:
  
  visual("Operações Matemáticas")
  operacao = int(input("""
  [1] Soma
  [2] Subtração
  [3] Multiplicação
  [4] Divisão
  [5] Exponenciação
  
Escolha a operação desejada[1000 para parar]: """))
  match operacao:
    case 1:
      soma = primeiro_numero + segundo_numero
      print(f"\033[1;32mA soma de {primeiro_numero:.0f} + {segundo_numero:.0f} = {soma:.0f}\033[m")
    case 2:
      subtracao = primeiro_numero - segundo_numero
      print(f"\033[1;33mA subtração de {primeiro_numero:.0f} - {segundo_numero:.0f} = {subtracao:.0f}\033[m")
    case 3:
      multiplicacao = primeiro_numero * segundo_numero
      print(f"\033[1;34mA multiplicação de {primeiro_numero} * {segundo_numero} = {multiplicacao:.2f}\033[m")
    case 4:
      divisao = primeiro_numero/segundo_numero
      print(f"\033[1;35mA divisão de {primeiro_numero} / {segundo_numero} = {divisao:.2f}\033[m")
    case 5:
      exponeciacao = primeiro_numero ** segundo_numero
      print(f"\033[1;30mA exponenciação de {primeiro_numero} ^ {segundo_numero} = {exponeciacao:.1f}\033[m")
    case 1000:
      break
     