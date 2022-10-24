# Exemplo de análise: relação entre renda e notas da redação do ENEM 2021

Este repositório contém os códigos usados nos resultados apresentados no artigos [Analisando dados do ENEM com Python](https://www.linkedin.com/pulse/analisando-dados-do-enem-com-python-vagner-bessa/?trackingId=3nRh3DmOSgKscv6ivhOtOg%3D%3D) e [Análise de dados do ENEM: Relação entre renda e nota da redação (Python e seaborn)](https://www.linkedin.com/pulse/an%25C3%25A1lise-de-dados-do-enem-rela%25C3%25A7%25C3%25A3o-entre-renda-e-nota-da-vagner-bessa)

## Uso

### Requisitos:

 - pandas: `python3 -m pip install pandas`
 - jupyter notebook: `python3 -m pip install jupyter`
 - matplotlib: `python3 -m pip install matplotlib`
 - seaborn: `python3 -m pip install seaborn`
 - pandas_read_ods: `python3 -m pip install git+https://github.com/bessavagner/pandas_ods_reader.git@skiprows`

### Dados:

Baixe os dados da página no INEP: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem.

Alternativamente, você pode usar os dados já selecionados contendo os valores de 'estado', 'nota' e 'renda' que estão no arquivo 'renda_redacao_2021.pkl'. Para isso, troque (ou comente) a segunda linha por:

```python
renda_redacao_= pd.read_pickle('renda_redacao_2021.pkl')
renda_redacao_.sample(5)
```