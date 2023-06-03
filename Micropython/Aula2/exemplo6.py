# IEA 2023
# Exemplo 6 - Aula 2
# 20 Fev 2023
# 107393 - Tomás Leite

# Módulo time

from time import sleep
from time import time
from time import gmtime
from time import localtime
from time import ticks_ms

inicio = ticks_ms()
for i in range(3):
    sleep (0.5)
    print (i)
    
fim = ticks_ms()
intervalo = fim - inicio
msg = 'Intervalo ms'
print ( msg, intervalo)

print (gmtime())
print (localtime())
