import random

random.seed(123)
precio_inicial = 135.51
mu = 0.00012
sigma = 0.035

variacion = random.normalvariate(mu, sigma)
precio_lunes = precio_inicial* (1 + variacion)

variacion = random.normalvariate(mu, sigma)
precio_martes = precio_lunes* (1 + variacion)

variacion = random.normalvariate(mu, sigma)
precio_miercoles = precio_martes* (1 + variacion)

variacion = random.normalvariate(mu, sigma)
precio_jueves = precio_miercoles* (1 + variacion)

variacion = random.normalvariate(mu, sigma)
precio_viernes = precio_jueves* (1 + variacion)

print(f"El precio de ggal el lunes es: {precio_lunes:.2f}")
print(f"El precio de ggal el martes es: {precio_martes:.2f}")
print(f"El precio de ggal el miercoles es: {precio_miercoles:.2f}")
print(f"El precio de ggal el jueves es: {precio_jueves:.2f}")
print(f"El precio de ggal el viernes es: {precio_viernes:.2f}")