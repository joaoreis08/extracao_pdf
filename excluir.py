from pathlib import Path
from datetime import datetime

def exclui_pdf():
    ano = datetime.now().year
    mes = str(datetime.now().month).zfill(2)
    dia = str(datetime.now().day).zfill(2)

    caminho_pdf = Path(f'PoderExecutivo({ano}{mes}{dia}).pdf')

    if caminho_pdf.exists():
        caminho_pdf.unlink()
