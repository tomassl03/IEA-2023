# IEA 2023
# Exercício 7 - Aula 2
# 20 Fev 2023
# 107393 - Tomás Leite

# Fazer os imports
from time import sleep
from time import time
from time import gmtime
from time import localtime
from time import ticks_ms

cc = 0 #Contagem começa a 0
aux = 'ON'

#Ciclo while para fazer pisca pisca
while cc<10:     #10 ciclos de mensagem 'On' e 'Off'
    cc = cc + 1   
    sleep (0.5)
    aux = 'OFF'   # 0.5s OFF
    print (aux)
    sleep (1)     # 1s ON 
    aux = 'ON'
    print (aux)