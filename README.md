# Extração de Dados de PDFs

Este projeto foi desenvolvido com o objetivo de extrair dados de decretos de arquivos PDF do Diário de Pernambuco e organizar essas informações em um arquivo Excel.

# Funcionalidades

Extração de Texto: Utiliza bibliotecas Python para extrair texto completo de arquivos PDF.
Identificação de Decretos: Processa e identifica decretos dentro do texto extraído usando padrões de expressões regulares.
Exportação para Excel: Organiza os decretos identificados em um DataFrame do Pandas e os exporta para um arquivo Excel (.xlsx).

## 🚀 Começando

Essas instruções permitem que você tenha uma cópia do projeto em sua máquina para testes e desenvolvimento.

### 📋 Pré-requisitos

Para rodar este projeto, você precisará do Python instalado. Além disso, é necessário instalar as dependências do projeto.

### 🔧 Instalando

1. Clone o repositório:
    ```bash
    git clone https://github.com/joaoreis08/extracao_pdf.git
    ```

2. Acesse a pasta do projeto:
    ```bash
    cd extracao_pdf
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Como rodar o projeto:
    ```bash
    python main.py
    ```

## 📦 Tecnologias

- Python

## 📑 Arquivos

- `main.py`: Arquivo principal para execução da extração.
- `extract.py`: Funções para extrair dados do PDF.
- `valores.py`: Contém valores usados no processo de extração.
- `excluir.py`: Funções para limpar dados extraídos (caso necessário).

## 🧑‍💻 Contribuindo

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Faça suas alterações.
4. Faça commit (`git commit -am 'Adiciona nova feature'`).
5. Envie para o repositório remoto (`git push origin feature/nome-da-feature`).
6. Abra um Pull Request.

## 📝 Licença

Este projeto está licenciado sob a licença XYZ - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
