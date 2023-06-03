# IEA 2023
# Exercício 2 - Aula 2
# 20 Fev 2023
# 107393 - Tomás Leite

# Criar 3 Funções :
# LerC() -> Leitura de Temperatura em ºC
# ConvCF(Celsius) -> Conversão ºC em ºF
# ConvCK(Celsius) -> Conversão ºC em K

def LerC():
    celsius = float(input ('Temperatura em ºC : '))
    return celsius
    
def ConvCF(celsius):
    faherenheit = celsius * (9/5) + 32
    return faherenheit

def ConvCK(celsius):
    kelvin = celsius + 237
    return kelvin

celsius = LerC()
faherenheit = ConvCF(celsius)
kelvin = ConvCK(celsius)

# Programa principal   
print ('''
        Opção F: Converter ºC em ºF
        Opção K: Converter ºC em K 
        ''')
option = input ( 'Opção : ')

if option == 'F' or option == 'f':
    print ('Temperatura em ºF : ',faherenheit)

elif option == 'K' or option == 'k':
    print ('Temperatura em K : ',kelvin)
    
else:       # Se o utilizador introduzir uma opção fora do esperado.... 
    print ('Erro na introdução de dados, tente de novo')
        