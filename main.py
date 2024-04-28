from datetime import datetime

nascencia = [
    {"dia": 3, "mes": 4, "ano": 2007}
]

dia = int(datetime.today().strftime("%d"))
mes = int(datetime.today().strftime("%m"))
ano = int(datetime.today().strftime("%Y"))


hoje = [
    {"dia": dia, "mes": mes, "ano": ano}
]


if hoje[0]["mes"] == nascencia[0]["mes"] and hoje[0]["dia"] == nascencia[0]["dia"]:
    print("feliz aniversario")
elif hoje[0]["mes"] >= nascencia[0]["mes"] and hoje[0]["dia"] > nascencia[0]["dia"]:
    print("seu aniversario ja passou")
elif hoje[0]["mes"] < nascencia[0]["mes"]:
    diferenca = nascencia[0]["mes"] - hoje[0]["mes"]
    print(f"seu aniversario é daqui {diferenca} mes")
elif hoje[0]["mes"] == nascencia[0]["mes"] and hoje[0]["dia"] < nascencia[0]["dia"]:
    diferenca = nascencia[0]["dia"] - hoje[0]["dia"]
    print(f"seu aniversario é daqui {diferenca} dias")
