import re
import pandas as pd
# Dicionário de meses para conversão de nome para número
meses = {
    "JANEIRO": "01", "FEVEREIRO": "02", "MARÇO": "03", "ABRIL": "04", "MAIO": "05", "JUNHO": "06",
    "JULHO": "07", "AGOSTO": "08", "SETEMBRO": "09", "OUTUBRO": "10", "NOVEMBRO": "11", "DEZEMBRO": "12",
    "janeiro": "01", "fevereiro": "02", "março": "03", "abril": "04", "maio": "05", "junho": "06",
    "julho": "07", "agosto": "08", "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12"
}

# Abrir o arquivo de texto
with open("Decretos.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Variáveis para armazenar os resultados
decretos = []
datas = []
valores = []

# Loop pelas linhas do arquivo
for i in range(len(linhas)):
    linha = linhas[i]
    if i == 0:
        
        num_doe = re.findall(r'(\d{2}) -',linha)
        num_doe = num_doe[0]
    
    # Verificar se a linha contém "DECRETO Nº"
    if "DECRETO Nº" in linha:
        # Usar regex para extrair o número completo após "DECRETO Nº", considerando pontos como separadores de milhar
        numero_decreto = re.search(r"DECRETO Nº\s*([\d\.]+)", linha)
        if numero_decreto:
            numero_decreto = numero_decreto.group(1)  # Captura o número completo, incluindo o ponto, se houver
        
        # Inicializar a data_formatada com valor padrão
        data_formatada = None
        
        # Usar regex para extrair a data do decreto no formato "DE xx DE MÊS DE yyyy"
        data_decreto = re.search(r"DE\s*(\d{2})\s*DE\s*([A-Za-zÁ-Úá-ú]+)\s*DE\s*(\d{4})", linha)
        if data_decreto:
            # Obter o dia, mês e ano
            dia = data_decreto.group(1)
            mes_texto = data_decreto.group(2)
            ano = data_decreto.group(3)
            
            # Converter o nome do mês para o número correspondente usando o dicionário
            mes_numero = meses.get(mes_texto.upper(), "00")  # Se não encontrar o mês, coloca "00" (erro)

            # Formatar a data no formato "DD/MM/YYYY"
            data_formatada = f"{dia}/{mes_numero}/{ano}"
        
        # Tentar pegar o valor "R$" na linha +2
        if i + 2 < len(linhas):  # Garantir que a linha +2 existe
            linha_valor = linhas[i + 2]
            valor = re.search(r"R\$\s*([\d\.,]+)", linha_valor)
            if valor:
                valor_extraido = valor.group(1)  # Captura o valor

                # Armazenar os resultados encontrados
                decretos.append(numero_decreto)
                # Verificar se data_formatada foi encontrada, senão adicionar uma data padrão
                datas.append(data_formatada if data_formatada else "Data não encontrada")
                valores.append(valor_extraido)

# Exibir resultados
for i in range(len(decretos)):
    print(f"DECRETO Nº {decretos[i]} - {datas[i]} - R$ {valores[i]} - Número_DOE: {num_doe}")
    
#df = pd.DataFrame("Decretos":[decretos],"data_decreto":[datas],"Valores":[valores],"Número_DOE:num_doe"