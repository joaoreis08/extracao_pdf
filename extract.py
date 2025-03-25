from datetime import datetime
import requests
from PyPDF2 import PdfReader

# URL do PDF (substitua as variáveis ano, mes, dia de acordo com o contexto)
ano = datetime.now().year
mes = str(datetime.now().month).zfill(2)
dia = str(datetime.now().day).zfill(2)

url = f"https://cepebr-prod.s3.amazonaws.com/1/cadernos/{ano}/{ano}{mes}{dia}/1-PoderExecutivo/PoderExecutivo({ano}{mes}{dia}).pdf"

# Passo 1: Baixar o PDF do site
response = requests.get(url)

# Verificar se o PDF foi baixado com sucesso
if response.status_code == 200:
    # Passo 2: Salvar o conteúdo do PDF em um arquivo local
    with open(f"PoderExecutivo({ano}{mes}{dia}).pdf", "wb") as f:
        f.write(response.content)  # Escreve o conteúdo binário no arquivo
    print("PDF salvo com sucesso.")
else:
    print("Falha ao baixar o PDF.")

# Inicializar a variável de texto total
texto_total = ""

# Passo 3: Abrir o PDF para extração de texto
with open(f"PoderExecutivo({ano}{mes}{dia}).pdf", "rb") as arquivo:  # Abrir o arquivo em modo binário de leitura
    leitor = PdfReader(arquivo)  # Usando PdfReader para ler o PDF

    # Passo 4: Percorrer as páginas e buscar a frase
    for pagina in leitor.pages:
        texto_pagina = pagina.extract_text()  # Extrair texto da página
        if texto_pagina and "Abre ao Orçamento Fiscal do Estado" in texto_pagina:
            texto_total += texto_pagina  # Acumula o texto das páginas que contêm a frase

# Passo 5: Exibir o texto extraído
# Salvar o texto extraído em um arquivo de texto
with open("Decretos.txt", 'w', encoding="utf-8") as decretos:
    decretos.write(texto_total)  # Escrever o texto no arquivo .txt
