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
        print('Lendo arquivo txt...')
        print(linhas)  # Verificar conteúdo do arquivo

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
                print(f"Decreto encontrado: {numero_decreto.group(1)}")  # Depuração

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
                    print(f"Data encontrada: {data_formatada}")  # Depuração
                else:
                    data_formatada = "Data não encontrada"  # Caso a data não seja encontrada

                # Agora, buscar o valor somente até encontrar outro "DECRETO Nº"
                for j in range(i + 1, len(linhas)):
                    linha_valor = linhas[j]
                    
                    # Verificar se encontramos um novo decreto (o valor só é válido se não houver outro decreto)
                    if "DECRETO Nº" in linha_valor:
                        print(f"Novo decreto encontrado: {linha_valor.strip()}")  # Depuração
                        break  # Se encontrar um novo decreto, interromper a busca pelo valor

                    # Procurar pela frase chave que indica o valor
                    if "Abre ao Orçamento Fiscal do Estado, relativo ao exercício de 2025, crédito suplementar no valor de R$" in linha_valor:
                        valor = re.search(r"R\$\s*([\d\.,]+)", linha_valor)
                        if valor:
                            valor_extraido = valor.group(1)  # Captura o valor após "R$"
                            print(f"Valor encontrado: {valor_extraido}")  # Depuração

                            # Armazenar os resultados encontrados
                            decretos.append(numero_decreto.group(1))
                            datas.append(data_formatada)
                            valores.append(valor_extraido)
                            # Adicionar o número do DOE a cada entrada
                            lista_decretos.append(numero_decreto.group(1))
                            lista_data.append(data_formatada)
                            lista_valores.append(valor_extraido)
                            lista_doe.append(num_doe)
                            break  # Encontrou o valor, não precisa procurar mais

    # Criar o DataFrame e salvar no Excel
    df = pd.DataFrame({
        "Decretos": lista_decretos,
        "Data_decreto": lista_data,
        "Valores": lista_valores,
        "Número_DOE": lista_doe
    })

    # Verificar se o DataFrame está vazio
    if df.empty:
        print("DataFrame está vazio!")
    else:
        print("DataFrame gerado com sucesso!")

    # Salvar no Excel
    df.to_excel(r"S:\SEPOC\07.DECRETOS_PL\2025\Acompanhamento Limite LOA 2025\decretos_extraidos.xlsx", index=False)

