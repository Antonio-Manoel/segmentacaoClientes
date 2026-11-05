from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

# coloque abaixo o caminho para os arquivos de dados de seu projeto
DADOS_ORIGINAIS = PASTA_DADOS / "Mall_Customers.csv"
DADOS_SEM_ID = PASTA_DADOS / "Mall_Customers_no_CustomerID.csv"
DADOS_SEM_ID_PREPROCESSADOS = PASTA_DADOS / "Mall_Customers_no_CustomerID_preprocessado.csv"