# IEA 2023
# Exemplo 8 - Aula 2
# 20 Fev 2023
# 107393 - Tomás Leite

# Módulo time (Python)

from datetime import datetime

# Leitura data e hora
now = datetime.now()
print ('Data e hora atual : ',now )

# Visualização data e hora com formatação
dh_f = now.strftime('%Y-%m-%d %H:%M:%S')
print ( 'Data e Hora (com formatação) : ', dh_f)