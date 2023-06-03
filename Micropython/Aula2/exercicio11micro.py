# IEA 2023
# Exercício 11 (MicroPython) - Aula 2
# 21 Fev 2023
# 107393 - Tomás Leite

# Programa para leitura entrada analógica
# ADC - Analogic Digital Converter
# Conversor analógico digital 0 a 3.3V
# 12 bits - 2**12 - 4096 pontos
# Corresponde a 3.3V / 4096 = 0.000805V


from machine import Pin, ADC

pot = ADC(Pin(33))  # criação do objeto
pot.atten (ADC.ATTN_11DB)  # range 0 - 3.3V

for i in range (100):
    xx = pot.read()
    print ('Valor ADC : ',xx)