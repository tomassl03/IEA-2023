# IEA 2023
# Exemplo 5 - Aula 2
# 20 Fev 2023
# 107393 - Tomás Leite

# Formatação de dados

a = 1234.9124
b = 455
print ('Valor de a : %5.2f <>' %(a))
print ('Valor de a e b : %5.1f <--> %5d <-->' %(a,b))
print ('Valor a - round ', round(a,2))

# Formatação
c = "Primeiro argumento : {0} segundo argumento : {1} ".format(27, 02)
print (c)

d = "Primeiro argumento : {0:5d} segundo argumento : {1:5.2f}"
print (d.format(b, a))