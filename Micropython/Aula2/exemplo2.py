# IEA 2023
# Exemplo 2 - Aula 2
# 20 Fev 2023
# 107393 - Tomás Leite

def PerimetroVolume (raio, altura):
    print ( 'Cálculo Perímetro/Volume Cilindro (usar .) ')
    per = 2 * 3.14 * float(raio)
    volume = per * float(altura)
    return per, volume


# Programa principal
print ( 'Cálculo perímetro e volume de um cilíndro : ')
a = input ( 'Introduza o raio do disco ? ')
b = input ( 'Introduza a altura do cilindro ? ')
rr,vv = PerimetroVolume (a,b)
print ( 'Perímetro do disco : ', rr)
print ( 'Volume do cilindro : ', vv)