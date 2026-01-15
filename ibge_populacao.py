import os
import requests
import pandas as pd


def get_populacao_municipios(uf_codigo: int, ano: int) -> pd.DataFrame:
    """
    Consulta a API do IBGE e retorna a população dos municípios de um estado.

    Parâmetros:
    uf_codigo (int): Código IBGE da UF (ex: 25 = Paraíba)
    ano (int): Ano da população (ex: 2022)

    Retorna:
    pd.DataFrame: DataFrame com Município e Habitantes
    """

    url = (
        f"https://servicodados.ibge.gov.br/api/v3/agregados/4709/"
        f"periodos/{ano}/variaveis/93?localidades=N6[N3[{uf_codigo}]]"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data_json = response.json()

    dados = []
    series = data_json[0]["resultados"][0]["series"]

    for item in series:
        municipio = item["localidade"]["nome"]
        habitantes = item["serie"].get(str(ano))

        dados.append({
            "Municipio": municipio,
            "Habitantes": habitantes
        })

    return pd.DataFrame(dados)


def salvar_excel(df: pd.DataFrame, uf_codigo: int, ano: int):
    """
    Salva o DataFrame em Excel na pasta data/
    """

    os.makedirs("data", exist_ok=True)

    caminho = f"data/populacao_municipios_uf{uf_codigo}_{ano}.xlsx"
    df.to_excel(caminho, index=False)

    print(f"Arquivo salvo em: {caminho}")


if __name__ == "__main__":
    # Exemplo: Paraíba (25) - 2022
    UF_CODIGO = 25
    ANO = 2022

    df_populacao = get_populacao_municipios(UF_CODIGO, ANO)
    salvar_excel(df_populacao, UF_CODIGO, ANO)
