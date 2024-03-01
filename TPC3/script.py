import sys
import re

text = sys.stdin.read()

# Captura de elementos on, off, numérico e =
result = re.findall(r'on|off|[+\-]?\d+|=', text, re.IGNORECASE)
result = [x.lower() for x in result]

# Soma todos os valores
soma = 0
on_off = True
for item in result:
    if item == '=':
        print(f"Soma = {soma}")
    elif item == 'on':
        on_off = True
    elif item == 'off':
        on_off = False
    elif on_off:
        soma += int(item)