# IEA 2023
# Exercicio 11 - Aula 2
# 21 Fev 2023
# 107393 - Tomás Leite


from time import localtime
from time import gmtime

dh = gmtime()

f = open ("Aula2_RegistoAlunosP.txt","w")
print ('Criação do ficheiro Ok...')
r = 0

while r<=10:
    try:
        r += 1
        r2 = str(r)
        nm = int(input ('Número mecanográfico : '))
        if len(nm) != 6:
            raise ValueError('O número mecanográfico deve ter 6 digitos')
        na = str(input ('Nome do aluno : '))
        dh_f = '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(dh.tm_year, dh.tm_mon, dh.tm_mday, dh.tm_hour, dh.tm_min, dh.tm_sec)
        b = 'Registo N : ' + r2 + ' ' + dh_f + '  ' + nm + ' - ' + na
        f.write (b)
        f.write ('\n')
    except:
        print ('Erro na introdução de dados...')

f.close()

print ('Visualização do registo dos alunos...')
with open('Aula2_RegistoAlunosP.txt','r') as f1:
    f2 = f1.read()
    print (f2)

print ('Fim programa...')


