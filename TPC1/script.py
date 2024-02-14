import sys

modalidades = []
aptidao = {"aptos": 0, "inaptos": 0}
etario = {}
atletas = 0

nmr_line = False
for line in sys.stdin:
    if nmr_line:
        info = line.split(",")

        # 1.
        modalidades.append(info[8])

        # 2.
        if info[12] == "true\n": aptidao.update({"aptos": aptidao.get("aptos") + 1})
        else: aptidao.update({"inaptos": aptidao.get("inaptos") + 1})
        atletas += 1

        # 3.
        faixa_etaria = int(info[5])//5
        etario[faixa_etaria*5] = info[5]
    else:
        nmr_line = True

# 1. Modalidades desportivas por ordem alfabética
print("Modalidades por ordem alfabética")
modalidades = list(dict.fromkeys(modalidades))
modalidades.sort()
for mod in modalidades:
    print("- " + mod)

# 2. Percentagem de atletas aptos e inaptos
print("\nPercentagem de atletas aptos e inaptos")
print(f"Nº de atletas: {atletas}")
print(f"Nº de atletas aptos: {aptidao.get('aptos')}")
print(f"Nº de atletas inaptos: {aptidao.get('inaptos')}")

# 3. Distribuição de atletas por escalão etário
print("\nDistribuição de atletas por escalão etário")
keys = list(etario.keys())
keys.sort()
etario = {i: etario[i] for i in keys}
for idade, qtd in etario.items():
    print(f"- [{idade}, {idade+4}]: {qtd}")