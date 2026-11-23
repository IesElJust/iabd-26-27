"""Crea un notebook menut i comprova l'execució des d'un nucli nou."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient

def main():
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    # El notebook conté tant la pregunta com el càlcul i la interpretació.
    nb = nbformat.v4.new_notebook(cells=[nbformat.v4.new_markdown_cell("# Consum d'aigua\nDades sintètiques. Pregunta: quin consum mitjà tenen cinc dies?"), nbformat.v4.new_code_cell("litres = [110, 125, 100, 140, 125]\nassert all(x >= 0 for x in litres)\nprint('Dies:', len(litres))"), nbformat.v4.new_code_cell("mitjana = sum(litres) / len(litres)\nprint('Mitjana:', mitjana)\nassert mitjana == 120"), nbformat.v4.new_markdown_cell("## Interpretació\nLa mitjana és de 120 litres/dia. Cinc dies no permeten estimar l'estacionalitat anual.")])
    nb.metadata['kernelspec'] = {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}
    nbformat.write(nb, out / 'aigua.ipynb')
    # Un nucli nou evita dependre de variables d’una sessió anterior.
    executed = NotebookClient(nb, timeout=60, kernel_name='python3', resources={'metadata': {'path': str(out)}}).execute()
    nbformat.write(executed, out / 'aigua-executat.ipynb')
    assert all((c.get('execution_count') is not None for c in executed.cells if c.cell_type == 'code'))
    print('Notebook creat i executat des de zero: mitjana 120 litres/dia')
if __name__ == '__main__':
    main()
