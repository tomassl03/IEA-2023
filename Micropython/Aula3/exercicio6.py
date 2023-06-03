# IEA 2023
# Exercicio 6 - Aula 3
# 27 Fev 2023
# 107393 - Tomás Leite

from machine import Pin, ADC
from time import sleep

# Configuração entrada analógica

port = ADC (Pin(33))
port.atten (ADC.ATTN_11DB)  # range 0..3.3V
pot.width (ADC.WIDTH_12BIT) # resolução 0-4096

xx = 0
while xx < 100:
    analog_In = pot.read() * 3.3 / 4096     # Leitura entrada analógica
    print ( 'Entrada Analógica 33 {:5.2f} '.format(analog_In) )
    sleep (0.25)
    xx += 1

print ( 'Fim programa ... ' )

