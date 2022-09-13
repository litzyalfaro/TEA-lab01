# Tendencias e Innovacion en Tecnologia Agricola (TEA)
from unicodedata import numeric


minutos_str = input("minutos jugados? ")
print(minutos_str)
print(type(minutos_str))
valorPorMinuto_str = input("valor por minuto? ")
print(valorPorMinuto_str)
print(type(valorPorMinuto_str))
numeric = [int(minutos_str)*int(valorPorMinuto_str)]
print(numeric)
