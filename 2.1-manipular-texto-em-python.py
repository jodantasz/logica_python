# AULA COMPLETA - STRING EM PYTHON

# - Criação de strings
# - Strings e multilinha
# - Índices e slices
# - Operações com strings
# - Imutabilidade
# - Métodos úteis
# - Formação de texto
# - Unicode e bytes

# -------------------------------------
# 1) CRIAÇÃO DE STRINGS
# -------------------------------------
# Strings são textos em python.
# Podem ser criadas usando aspas simples ou duplas

texto1 = "Python"
texto2 = 'Curso de Python'
texto3 = "Copa 'padrão fifa'"
texto4 = 'Copa "padrão fifa"'

print (texto1, texto2, texto3, texto4)

# Python permite misturar aspas simples e duplas, dentro das strings sem precisae escapar caractéres

# ------------------------------------
# 2) STRINGS MULTILINHA
# ------------------------------------
#  Usando três aspas (""" ou ''') para criar textos que ocupam várias linhas.

menu = """\
Uso : programa [OPÇÕES]
-h Exibe ajuda
-U Url do dataset
"""
print (menu)

# - Esse formato é muito usado para:
# - Menus
# - Documentos
# - Textos longos

# ------------------------------------
# 3) CONCATENAÇÃO AUTOMÁTICA
# ------------------------------------
# Quando dus strings aparecem lado a lado o python junta automaticamnte

texto = ("Copa " "2026 " "Neymar é show mesmo? " "CONCERTEZA")
print(texto)

# ------------------------------------
# 4) STRINGS COMO SEQUÊNCIAS
# ------------------------------------
# Uma string funciona como uma sequência de caracteres, cada caractere possui um índice

st = "maracanã"
print ("Primeira Letra", st[0])
# só exibir a letra: M

print ("Última Letra", (st[-1]))

print ("Trecho 1:4", st[1:4])

print ("Do inicio até 3:", st[:3])

print ("Do 2 até o fim", st[2:])

print ("Tamanho:", len(st))
