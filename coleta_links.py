import os
import requests
import pandas as pd


def google_search(query: str, api_key: str, cse_id: str) -> str | None:
    """
    Realiza uma busca via Google Custom Search API
    e retorna o primeiro link encontrado.
    """

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cse_id
    }

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    if "items" in data and len(data["items"]) > 0:
        return data["items"][0]["link"]

    return None


def coletar_links_camaras(municipios: list[str]) -> pd.DataFrame:
    """
    Coleta os links dos sites das Câmaras Municipais
    a partir de uma lista de municípios.
    """

    api_key = os.getenv("GOOGLE_API_KEY")
    cse_id = os.getenv("GOOGLE_CSE_ID")

    if not api_key or not cse_id:
        raise EnvironmentError(
            "Defina as variáveis de ambiente GOOGLE_API_KEY e GOOGLE_CSE_ID."
        )

    resultados = []

    for municipio in municipios:
        query = f"Câmara Municipal de {municipio}"
        link = google_search(query, api_key, cse_id)

        resultados.append({
            "Municipio": municipio,
            "Link_Camara": link
        })

    return pd.DataFrame(resultados)


def salvar_excel(df: pd.DataFrame):
    """
    Salva o resultado em Excel na pasta data/
    """

    os.makedirs("data", exist_ok=True)
    caminho = "data/links_camaras_municipais.xlsx"
    df.to_excel(caminho, index=False)

    print(f"Arquivo salvo em: {caminho}")


if __name__ == "__main__":

    municipios = [
        "São Vicente do Seridó - PB", "Serra Branca - PB", "Serra da Raiz - PB",
        "Serra Grande - PB", "Serra Redonda - PB", "Serraria - PB",
        "Sertãozinho - PB", "Sobrado - PB", "Solânea - PB",
        "Soledade - PB", "Sossêgo - PB", "Sousa - PB",
        "Sumé - PB", "Tacima - PB", "Taperoá - PB",
        "Tavares - PB", "Teixeira - PB", "Tenório - PB",
        "Triunfo - PB", "Uiraúna - PB", "Umbuzeiro - PB",
        "Várzea - PB", "Vieirópolis - PB", "Zabelê - PB"
    ]

    df_links = coletar_links_camaras(municipios)
    salvar_excel(df_links)
