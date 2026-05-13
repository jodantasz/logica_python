#AULA COMPLETA: NÚMEROS EM PYTHON    

"""
O que vamos aprender?
1- Tipos numéricos
2- Conversão de tipos
3- Hierarquia numérica
4- Operações Matemáticas
5- Coerção de tipos
6- Verificação de tipos
7- Entrada de dados
"""
#===========================
## PASSO 1 - TIPOS NUMÉRICOS
# INT > numeros inteiros
# float > numeros com casas decimais
# complex > números complexos (usado em matemática/engenharia)

print ("==== TIPOS NUMÉRICOS ====")

# EXEMPLO O1 - NUMERO INTEIRO

# criamos uma variável chamada "numero_inteiro"
numero_inteiro = 10

#mostramos o valor 
print ("Valor:", numero_inteiro)

# type() mostra qual é o tipo da variável
print ("Tipo:", type (numero_inteiro))

print ("==========================================")

#EXEMPLO 2 - NUMERO DECIMAL

# Float é um numero com ponto decimal
numero_decimal = 3.14

print("Valor:", numero_decimal)
print ("tipo:", type (numero_decimal))

print ("==========================================")

#EXEMPLO 3 - NUMEROS COMPLEXOS
# Um numero complexo possui duas partes:
# Parte real (numero normal)
# Parte imaginário (multiplicada por j)

# Estrutura Geral:
# numero = a + bj

# a = parte real
# b = parte imaginaria
# j = unidade imaginaria

numero_complexo = 2 + 3j

print ("Valor:", numero_complexo)
print ("Tipo:", type(numero_complexo))

print ("=============================================")

# EXEMPLO 03 - ACESSANDO CADA PARTE DO NÚMERO 

# .REAL RETORNA A PARTE REAL
print ("Parte Real:", numero_complexo.real)

#.imag retorna a parte imaginária
print ("Parte Imaginária:", numero_complexo.imag)

#=======================================================
## PASSO 02 - CONVERSÃO TIPOS
#=======================================================

## Exemplo Clássico:
## Dados vindos do usuário são texto (string), muitas vezes é neccesário converter eles.

print ("===== Conversões ======")

# Float -> int

valor = int(3.9)

print ("int(3.9):", valor)
print ("Tipo:", type(valor))

#string -> int
valor1 = "10"
print (type(valor1))

valor2 = int ("10")
print ('int("10"):', valor)
print ("tipo:", type(valor2))

#int -> float
valor3 = float(10)
print ("float(10):", valor3)
print ("Tipo:", type(valor3))