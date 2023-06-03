# IEA 2023
# Exemplo 4 - Aula 3
# 27 Fev 2023
# 107393 - Tomás Leite

# Leitura de entrada Digital

from machine import Pin
from time import sleep

# Config Pin - PULL_DOWN (desligado)
button = Pin (15, Pin.IN, Pin.PULL_DOWN )

while True:
    sleep (0.5)
    if button.value():
        xx = 'Ligado'
    else:
        xx = 'Desligado'
    
    print ( 'Estado entrada 15 (GPI015) : {:1d} - {}'.format(button.value(),xx))