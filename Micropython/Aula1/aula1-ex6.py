# IEA 2023
# Aula 1 - Ex6
# 13 Fev 2023
# 107393 - Tomás Leite

while True:
    
    celsius = float(input ('Temperatura em ºC: '))
    
    print ('''
    Opção F: Converter ºC em ºF
    Opção K: Converter ºC em K ''')

    option = input('Opção: ')

    if option == 'F' or option == 'f':
        faherenheit = celsius*(9/5)+32
        print ('Temperatura em Faherenheit : ',faherenheit)
        
    elif option == 'K' or option == 'k':
        kelvin = celsius + 237
        print ('Temperatura em Kelvin : ' ,kelvin)
        
    else:
        print ('Escolha uma opção válida')
    
    print ()
    answer = input ('Pretende continuar (s/n) ? ')
    
    if answer == 'n':
        break
                    