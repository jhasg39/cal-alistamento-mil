from datetime import date, datetime

hoje = date.today()
entrada = input("Data de nascimento (dd/mm/aaaa): ")

nasc = datetime.strptime(entrada, "%d/%m/%Y").date()
data_18 = date(nasc.year + 18, nasc.month, nasc.day)

idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))

print(f"\nQuem nasceu em {nasc.strftime('%d/%m/%Y')} tem {idade} anos hoje ({hoje.strftime('%d/%m/%Y')}).")

if hoje == data_18:
    print("Hoje você completa 18 anos! Deve se alistar IMEDIATAMENTE!")
else:
    inicio, fim = (hoje, data_18) if hoje < data_18 else (data_18, hoje)
    anos = fim.year - inicio.year
    meses = fim.month - inicio.month
    dias = fim.day - inicio.day

    if dias < 0:
        meses -= 1
        ultimo_dia_mes_ant = (date(fim.year, fim.month, 1) - date.resolution).day
        dias += ultimo_dia_mes_ant

    if meses < 0:
        anos -= 1
        meses += 12

    if hoje < data_18:
        print("Você ainda NÃO pode se alistar (ainda não completou 18 anos).")
        print(f"Faltam {anos} ano(s), {meses} mês(es) e {dias} dia(s) para o seu alistamento.")
        print(f"Você completará 18 anos em {data_18.strftime('%d/%m/%Y')}.")
    else:
        print("Você JÁ PASSOU do período de alistamento obrigatório e não pode mais se alistar no prazo regular.")
        print(f"Você completou 18 anos há {anos} ano(s), {meses} mês(es) e {dias} dia(s).")
        print(f"Seu aniversário de 18 anos foi em {data_18.strftime('%d/%m/%Y')}.")
