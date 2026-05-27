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

# ------------------------------------
# 5) OPERAÇÕES COM STRINGS
# ------------------------------------
# Python permite várias operações com strings

print("m" in st)
# Significa que a letra "m" existe dentro da string

print("x" not in st)
# Significa que a letra "m" não existe dentro da string   

print("m" * 20)  
# Multiplica o que está na string

print("m" + "aracanã")
# soma a string (operador + concatena)

# ------------------------------------
# 6) Imutabilidade
# ------------------------------------

# Strings não podem ser alteradas diretamente"
# Isso significa que o conteúdo original não muda.
# Oque acontece é a criação de uma nova string.

texto6 = "python 3"

# Método replace cria uma nova string
texto6 = texto6.replace("3", "2")
print(texto6)

# ------------------------------------
# 7) MÉTODOS ÚTEIS
# ------------------------------------
# Strings possuem vários métodos úteis

cidade = "maracanã"
# Coloca a primeira letra em maiúsculo
cidade = (cidade.capitalize())

# conta quantas vezes "a" aparece.
print(cidade.count("a"))

# Verificar se começa com "m"
print(cidade.startswith("m"))

# Verifica se termina com "z"
print (cidade.endswith("z"))

frase = "copa de 2002"

# divide a string em uma lista
print(frase.split(" "))


# ------------------------------------
# 8) FORMAÇÃO DE STRINGS
# ------------------------------------
