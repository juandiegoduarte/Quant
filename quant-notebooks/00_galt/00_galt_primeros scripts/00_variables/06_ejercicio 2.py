ticker = "GFGC155.AG"

subyacente = ticker[:3]
print(subyacente)

posicion = ticker.find(".")
ultimos = ticker[posicion +1:]
print(ultimos)