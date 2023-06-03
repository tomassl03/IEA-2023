# IEA 2023
# Exercicio 7 - Aula 3
# 5 Mar 2023
# 107393 - Tomás Leite


import machine
import math

# Definir a entrada analógica do ESP32
adc = machine.ADC(machine.Pin(34))
adc.atten(machine.ADC.ATTN_11DB) # definir a atenuação do sinal
adc.width(machine.ADC.WIDTH_12BIT) # definir a resolução do conversor

# Parâmetros do termopar tipo J
A = 0.0012858
B = 0.0002387
C = 0.000000101

# Função para converter o valor da entrada analógica em mV
def convert_to_mv(value):
    return (value * 3300) / 4095

# Função para converter o valor de mV para ºC
def convert_to_celsius(mv):
    uV = mv * 1000
    uV2 = uV * uV
    uV3 = uV2 * uV
    return A + B*uV + C*uV2 + ((uV3-128000*uV2+25000000*uV)/1562500)

# Loop principal do programa
while True:
    # Lendo o valor da entrada analógica e convertendo para mV
    value = adc.read()
    mv = convert_to_mv(value)

    # Amplificação de ganho 200
    mv = mv / 200.0

    # Convertendo para temperatura em graus Celsius
    temp = convert_to_celsius(mv)

    print("Temperatura: {:.2f}ºC".format(temp))

    # Delay de 1 segundo
    machine.delay(1000)


# Configuramos a entrada analógica do ESP32 (pin 34) para ler valores com resolução de 12 bits e atenuação de 11 dB.
# Definimos os parâmetros A, B e C do polinômio de conversão para o termopar tipo J.
# Criamos duas funções: convert_to_mv converte o valor da entrada analógica em mV, e convert_to_celsius converte o valor de mV para graus Celsius utilizando o polinômio de conversão.
# No loop principal do programa, lemos o valor da entrada analógica, convertemos para mV, amplificamos por 200, e em seguida convertemos para graus Celsius utilizando a função convert_to_celsius. 
# Imprimimos o valor da temperatura no terminal e aguardamos 1 segundo antes de repetir o processo.