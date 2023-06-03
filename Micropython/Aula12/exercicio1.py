# IEA 2023
# Exercicio 1 - Aula 12
# 30 Mai 2023
# 107393 - Tomás Leite


from time import sleep  # Importa a função sleep do módulo time
from machine import Pin, ADC  # Importa as classes Pin e ADC do módulo machine



pot = ADC(Pin(33))  # Cria um objeto ADC conectado ao pin GPIO 33
pot.atten(ADC.ATTN_11DB)  # Define a atenuação do ADC (faixa completa de 3,3V)
pot.width(ADC.WIDTH_12BIT)  # Define a resolução do ADC para 12 bits (0..4096)

aux = 0  # Inicia uma variável auxiliar com valor 0
while aux < 1000:  # Repete o seguinte bloco de código enquanto aux for menor que 1000
    sleep(0.05)  # Aguarda 0,05 segundos (50 milissegundos)

    # Leitura da Entrada Analógica // potenciômetro
    xx = pot.read()  # Lê o valor do ADC, que corresponde à posição do potenciômetro, e armazena na variável xx

    aux += 1  # Incrementa o valor da variável aux em 1
    print('aux:', aux, 'Valor ADC:', xx, 'V in:', xx * 0.000805, 'V')  # Imprime os valores de aux, xx e a voltagem de entrada correspondente a xx em volts
