from valores import gera_excel
from extract import extracao_diario
from excluir import exclui_pdf

def main():
    extracao_diario()
    gera_excel()
    exclui_pdf()

if __name__ == '__main__':
    main()
