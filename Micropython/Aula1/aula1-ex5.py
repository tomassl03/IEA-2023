# IEA 2023
# Aula 1 - Ex5
# 13 Fev 2023
# 107393 - Tomás Leite


celsius = float(input('Qual a temperatura em ºC: '))

print ('''
Opção F: Converter ºC em ºF
Opção K: Converter ºC em K ''')

option = input('Opção: ')

if option == 'F' or option == 'f':
    faherenheit = celsius*(9/5)+32
    print (faherenheit)
elif option == 'K' or option == 'k':
    kelvin = celsius + 237
    print (kelvin)
else:
    print ('Escolha uma opção válida')
