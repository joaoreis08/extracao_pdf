import re
import pandas as pd

def gera_excel():
    meses = {
        "JANEIRO": "01", "FEVEREIRO": "02", "MARÇO": "03", "ABRIL": "04", "MAIO": "05", "JUNHO": "06",
        "JULHO": "07", "AGOSTO": "08", "SETEMBRO": "09", "OUTUBRO": "10", "NOVEMBRO": "11", "DEZEMBRO": "12",
        "janeiro": "01", "fevereiro": "02", "março": "03", "abril": "04", "maio": "05", "junho": "06",
        "julho": "07", "agosto": "08", "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12"
    }

    with open("extracao.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        print('Lendo arquivo txt...')

    decretos = []
    datas = []
    valores = []
    lista_decretos = []
    lista_data = []
    lista_valores = []
    lista_doe = []
    lista_publicacao = []

    for i in range(len(linhas)):
        linha = linhas[i]
        if i == 0:
            num_doe = re.findall(r"N\u00C0\s*(\d+)", linha)
            data_publicacao = re.search(r"\s*(\d{1,2})\s*de\s*([A-Za-zÁ-Úá-ú]+)\s*de\s*(\d{4})", linha)
            if num_doe:
                num_doe = num_doe[0]
                print(f"DOE encontrado: {num_doe}")
            if data_publicacao:
                dia_publicacao = data_publicacao.group(1).zfill(2)
                mes_publicacao = meses.get(data_publicacao.group(2).upper(), "00")
                ano_publicacao = data_publicacao.group(3)
                data_de_publicacao = f"{dia_publicacao}/{mes_publicacao}/{ano_publicacao}"
                print(f"Data de publicação encontrada: {data_de_publicacao}")

        if "DECRETO Nº" in linha:
            numero_decreto = re.search(r"DECRETO Nº\s*([\d\.]+)", linha)
            if numero_decreto:
                print(f"Decreto encontrado: {numero_decreto.group(1)}")

                data_decreto = re.search(r"s*(\d{1,2})\s*DE\s*([A-Za-zÁ-Úá-ú]+)\s*DE\s*(\d{4})", linha)
                if data_decreto:
                    dia = data_decreto.group(1)
                    dia = dia.zfill(2)
                    mes_texto = data_decreto.group(2)
                    ano = data_decreto.group(3)
                    mes_numero = meses.get(mes_texto.upper(), "00")
                    data_formatada = f"{dia}/{mes_numero}/{ano}"
                    print(f"Data encontrada: {data_formatada}")
                else:
                    data_formatada = "Data não encontrada"

                for j in range(i + 1, len(linhas)):
                    linha_valor = linhas[j]

                    if "DECRETO Nº" in linha_valor:
                        break

                    if "crédito suplementar no valor de R$" in linha_valor:
                        valor = re.search(r"R\$\s*([\d\.,]+)", linha_valor)
                        if valor:
                            valor_extraido = valor.group(1)
                            print(f"Valor encontrado: {valor_extraido}")

                            decretos.append(numero_decreto.group(1))
                            datas.append(data_formatada)
                            valores.append(valor_extraido)
                            lista_decretos.append(numero_decreto.group(1))
                            lista_data.append(data_formatada)
                            lista_valores.append(valor_extraido)
                            lista_doe.append(num_doe)
                            lista_publicacao.append(data_de_publicacao)
                            break

    df = pd.DataFrame({
        "Decretos": lista_decretos,
        "Data_decreto": lista_data,
        "Valores": lista_valores,
        "Número_DOE": lista_doe,
        "Data_publi": data_de_publicacao
    })

    print(f"Listas antes do DataFrame - Decretos: {lista_decretos}, Datas: {lista_data}, Valores: {lista_valores}, DOE: {lista_doe}, Data_publi: {data_de_publicacao}")

    if df.empty:
        print("DataFrame está vazio!")
    else:
        print("DataFrame gerado com sucesso!")
    # Salvar no Excel
    df.to_excel(r"S:\SEPOC\07.DECRETOS_PL\2025\Acompanhamento Limite LOA 2025\decretos_extraidos.xlsx", index=False)

