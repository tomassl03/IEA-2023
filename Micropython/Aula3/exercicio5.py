# IEA 2023
# Exercicio 5 - Aula 3
# 27 Fev 2023
# 107393 - Tomás Leite

# Semáforos

from time import sleep
from machine import Pin

# Config porta G2, G4 e G5 como Pinos de saída
led_green = Pin (2, Pin.OUT)
led_yellow = Pin (4, Pin.OUT)
led_red = Pin (5, Pin.OUT)

# Config GPI015
button = Pin ( 15, Pin.IN, Pin.PULL_DOWN )


xx = input ( 'Digite uma tecla para iniciar : ' )

aux = 0
while True:
    sleep (0.5)
    aux += 1
    if button.value():
        axu = 'Button : 0'
    else:
        axu = 'Button : 1'
    if aux in range (0,9):
        led_green.value (True)
        led_yellow (False)
        led_red (False)
    elif aux in range (10,12):
        led_green.value (False)
        led_yellow.value (True)
        led_red.value (False)
    elif aux in range (13,18):
        led_green.value (False)
        led_yellow.value (False)
        led_red.value (True)
    elif aux > 19:
        aux = 0
        
    print ( 'Estado : ', aux , axu , 'Verde : ', led_green.value(), '      ', 'Amarelo : ', led_yellow.value(), '      ', 'Vermelho : ', led_red.value())
    
