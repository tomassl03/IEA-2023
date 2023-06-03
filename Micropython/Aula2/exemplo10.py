# IEA 2023
# Exemplo 10 - Aula 2
# 20 Fev 2023
# 107393 - Tomás Leite

# MicroPython: Escrita e Leitura em Ficheiro
print ('Escrita em ficheiro de texto...' )

f = open ('IEA_Aula2.txt','w')
print ( 'Abertura de ficheiro Ok...')

# Escrita sequencial de 10 linhas no ficheiro de texto
for i in range(10):
    a = 'Linha : ' + str(i) + '\n'
    f.write (a)
    print (a)

f.write ('\n') # mudar de linha
f.close
print ()

# Leitura do ficheiro de texto
print ('Leitura de um ficheiro de texto...')
f1 = open ( 'IEA_Aula2.txt','r')
xx = f1.read()
print (xx)
f1.close
print ('Fim programa...')