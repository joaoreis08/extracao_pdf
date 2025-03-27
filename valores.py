import re
import pandas as pd

def gera_excel():
    # Dicionário de meses para conversão de nome para número
    meses = {
        "JANEIRO": "01", "FEVEREIRO": "02", "MARÇO": "03", "ABRIL": "04", "MAIO": "05", "JUNHO": "06",
        "JULHO": "07", "AGOSTO": "08", "SETEMBRO": "09", "OUTUBRO": "10", "NOVEMBRO": "11", "DEZEMBRO": "12",
        "janeiro": "01", "fevereiro": "02", "março": "03", "abril": "04", "maio": "05", "junho": "06",
        "julho": "07", "agosto": "08", "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12"
    }

    # Abrir o arquivo de texto
    with open("extracao.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    # Variáveis para armazenar os resultados
    decretos = []
    datas = []
    valores = []
    lista_decretos = []
    lista_data = []
    lista_valores = []
    lista_doe = []
    
    # Extração do número do DOE da primeira linha
    for i in range(len(linhas)):
        linha = linhas[i]
        if i == 0:  # Captura o número do DOE na primeira linha
            num_doe = re.findall(r"NÀ\s*(\d+)", linha)
            if num_doe:
                num_doe = num_doe[0]

        # Verificar se a linha contém "DECRETO Nº"
        if "DECRETO Nº" in linha:
            # Usar regex para extrair o número completo após "DECRETO Nº"
            numero_decreto = re.search(r"DECRETO Nº\s*([\d\.]+)", linha)
            if numero_decreto:
                numero_decreto = numero_decreto.group(1)  # Captura o número completo, incluindo o ponto, se houver

            # Usar regex para extrair a data do decreto no formato "DE xx DE MÊS DE yyyy"
            data_decreto = re.search(r"DE\s*(\d{2})\s*DE\s*([A-Za-zÁ-Úá-ú]+)\s*DE\s*(\d{4})", linha)
            if data_decreto:
                # Obter o dia, mês e ano
                dia = data_decreto.group(1)
                mes_texto = data_decreto.group(2)
                ano = data_decreto.group(3)

                # Converter o nome do mês para o número correspondente
                mes_numero = meses.get(mes_texto.upper(), "00")

                # Formatar a data no formato "DD/MM/YYYY"
                data_formatada = f"{dia}/{mes_numero}/{ano}"
            else:
                data_formatada = "Data não encontrada"  # Caso a data não seja encontrada

            # Verificar se existe uma linha +2 para pegar o valor
            if i + 2 < len(linhas):  
                linha_valor = linhas[i + 2]
                valor = re.search(r"R\$\s*([\d\.,]+)", linha_valor)
                if valor:
                    valor_extraido = valor.group(1)  # Captura o valor após "R$"

                    # Armazenar os resultados encontrados
                    decretos.append(numero_decreto)
                    datas.append(data_formatada)
                    valores.append(valor_extraido)
                    # Adicionar o número do DOE a cada entrada
                    lista_decretos.append(numero_decreto)
                    lista_data.append(data_formatada)
                    lista_valores.append(valor_extraido)
                    lista_doe.append(num_doe)

    # Criar o DataFrame e salvar no Excel
    df = pd.DataFrame({
        "Decretos": lista_decretos,
        "Data_decreto": lista_data,
        "Valores": lista_valores,
        "Número_DOE": lista_doe
    })

    # Salvar o DataFrame como arquivo Excel
    df.to_excel(r'S:\SEPOC\07.DECRETOS_PL\2025\Acompanhamento Limite LOA 2025\decretos_extraidos.xlsx', index=False)

