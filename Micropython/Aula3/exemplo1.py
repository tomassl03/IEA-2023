# IEA 2023
# Exemplo 1 - Aula 3
# 27 Fev 2023
# 107393 - Tomás Leite

# Módulo Time

from time import sleep
from time import gmtime
from time import localtime

# Leitura data e hora

dh = gmtime()
print ( 'Data e Hora atual : ', dh )

# Visualização data e hora com formatação
dh_f = '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(dh[0],dh[1],dh[2],dh[3],dh[4],dh[5])
print ( 'Data e Hora (com formatação) : ', dh_f)