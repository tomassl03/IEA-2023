# IEA 2023
# Exemplo 2 - Aula 3
# 27 Fev 2023
# 107393 - Tomás Leite

# Led pisca/pisca

from time import sleep
from machine import Pin

# configuração pin de saída

led = Pin (2,Pin.OUT )
led.value ( True )

xx = input ( 'Digite uma tecla para iniciar : ' )
aux = 0

while True:
    led.value ( not led.value() )
    sleep (0.5)
    aux += 1
    print ( aux, ' -> ', bool(led.value()) )

