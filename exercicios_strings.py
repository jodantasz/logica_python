# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

print ("MÓDULO 1 — CRIAÇÃO DE STRINGS")
print ("--------------------------------------------------------")

# EX1
# Crie uma variável chamada texto1 com o valor "Logica" usando aspas duplas e exiba o conteúdo.

print ("EX1")
texto1 = "lógica"
print (texto1)
print ("--------------------------------------------------------")

# EX2
# Crie uma variável chamada texto2 com o valor 'Eu sou top em python' usando aspas simples e exiba.

print ("EX2")
texto2 = 'Eu sou top em python'
print (texto2)
print ("--------------------------------------------------------")

# EX3
# Crie uma string usando aspas simples que contenha aspas duplas dentro do texto: copa "padrão fifa".

print ("EX3")
st = 'copa "padrão fifa"'
print(st)
print ("--------------------------------------------------------")

# EX4
# Crie uma string usando aspas duplas que contenha aspas simples dentro do texto: copa 'padrão fifa'.

print ("EX4")
st = "copa 'padrão fifa'"
print (st)
print ("--------------------------------------------------------")

# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

print ("MÓDULO 2 — STRINGS MULTILINHA")
print ("--------------------------------------------------------")

# EX5
# Crie uma string multilinha representando um menu com as opções:
# -A  Exibe ajuda
# -E  Execute agora, quero jogar!

print ("EX5")

menu = """\
Uso : programa [OPÇÕES]
-A Exibe ajuda
-E Execute agora, quero jogar!
"""
print (menu)
print ("--------------------------------------------------------")

# EX6
# Crie uma string multilinha contendo um poema com três versos.

print ("EX6")
poema = """\
Saudade é solidão acompanhada,
é quando o amor ainda não foi embora,
mas o amado já.
"""
print (poema)
print ("--------------------------------------------------------")


# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

print ("MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA")
print ("--------------------------------------------------------")

# EX7
# Use concatenação automática de literais para unir as palavras "Volei" e "top!".

print ("EX7")
texto = ("Vôlei " "é " "Top!")
print(texto)
print ("--------------------------------------------------------")

# EX8
# Concatene automaticamente as strings "Python", " é ", "demais" em uma única string.

print ("EX8")
st = ("Python" " é " "demais")
print (st)
print ("--------------------------------------------------------")

# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

print ("MÓDULO 4 — STRINGS COMO SEQUÊNCIAS")
print ("--------------------------------------------------------")

# EX9
# Atribua "software" a uma variável chamada st
# e mostre a primeira letra da string.

print ("EX9")
st = "software"
print ("Primeira Letra", st[0])
print ("--------------------------------------------------------")

# EX10
# Usando a mesma string "software", mostre a última letra.

print ("EX10")
st = "software"
print ("Última Letra", st[-1])
print ("--------------------------------------------------------")

# EX11
# Mostre os caracteres do índice 1 até o índice 4 (sem incluir o 4) da string " software ".

print ("EX11")
st = "software"
print ("Trecho 1:4", st[1:4])
print ("--------------------------------------------------------")

# EX12
# Mostre os caracteres do início até o índice 3 da string "software".

print ("EX12")
st = "software"
print ("Trecho :3", st[:3])
print ("--------------------------------------------------------")

# EX13
# Mostre os caracteres do índice 2 até o final a string "software".

print ("EX13")
st = "software"
print (st[2:])
print ("--------------------------------------------------------")

# EX14
# Mostre o tamanho da string "software" usando função len().

print ("EX14")
st = "software"
print ("Tamanho:", len(st))
print ("--------------------------------------------------------")

# EX15
# Acesse o último caractere de "software" usando índice positivo (sem usar -1).

print ("EX15")
st = "software"
print ("Última Letra:", st[7])
print ("--------------------------------------------------------")

# EX16
# Mostre os caracteres que estão nos índices pares da string "software".

print ("EX16")
st = "software"
print ("Índices pares:", st[::2])
print ("--------------------------------------------------------")

# EX17
# Inverta a string "software".

print ("EX17")
texto = "software"
texto_invertido = texto[::-1]
print(texto_invertido)
print ("--------------------------------------------------------")