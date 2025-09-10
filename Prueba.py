# reto3.py  —  sin arreglos/listas: dos pasadas sobre la MISMA entrada
import sys, re

# Genera un iterador de tokens numéricos (como strings) sobre todo stdin
def token_iter(s):
    return (m.group(0) for m in re.finditer(r'-?\d+(?:\.\d+)?', s))

data = sys.stdin.read()

# ---------- 1ª pasada: calcular promedios ----------
it1 = token_iter(data)

N = int(next(it1))
sumH = cntH = 0
sumM = cntM = 0

for _ in range(N):
    hemog = float(next(it1))
    gen   = int(next(it1))
    if gen == 1:
        sumH += hemog; cntH += 1
    elif gen == 2:
        sumM += hemog; cntM += 1

promH = sumH / cntH if cntH else 0.0
promM = sumM / cntM if cntM else 0.0

# etiquetas por promedio
def etiqueta_h(prom):
    if prom < 12.2: return "Baja"
    elif prom <= 16.6: return "Normal"
    else: return "Alta"

def etiqueta_m(prom):
    if prom < 12.6: return "Baja"
    elif prom <= 15: return "Normal"
    else: return "Alta"

etH = etiqueta_h(promH)
etM = etiqueta_m(promM)

# ---------- 2ª pasada: contar > / < / = al promedio ----------
it2 = token_iter(data)

_ = int(next(it2))  # N nuevamente

encH = debH = igH = 0
encM = debM = igM = 0

for _ in range(N):
    hemog = float(next(it2))
    gen   = int(next(it2))
    if gen == 1:
        if hemog > promH: encH += 1
        elif hemog < promH: debH += 1
        else: igH += 1
    elif gen == 2:
        if hemog > promM: encM += 1
        elif hemog < promM: debM += 1
        else: igM += 1

# ---------- salidas ----------
print(f"{promH:.2f} {etH}")
print(f"{promM:.2f} {etM}")
print(f"{encH} {encM}")
print(f"{debH} {debM}")
print(f"{igH} {igM}")
