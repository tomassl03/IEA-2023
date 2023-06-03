# IEA 2023
# Exemplo 12 - Aula 2
# 21 Fev 2023
# 107393 - Tomás Leite


# LED Pisca Pisca 0.5s 

from time import sleep
from machine import pin

# Configuração da entrada
led = pin ( 2, Pin.OUT)
led.value (True)
aux = True

xx = input ('Inicio : ')

while True:
    led.value ( not led.value() )
    aux = not aux
    sleep (0.5)
    print ( 'Pisca Pisca : ', aux)