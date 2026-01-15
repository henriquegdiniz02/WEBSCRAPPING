import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

COOKIES = dict(cookie="value")


def acessar_site(url: str) -> BeautifulSoup | None:
    """
    Acessa um site e retorna o BeautifulSoup do HTML.
    """
    try:
        response = requests.get(url, headers=HEADERS, cookies=COOKIES, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except Exception:
        return None


def existe_texto(soup: BeautifulSoup, termos: list[str]) -> int:
    """
    Verifica se algum dos termos aparece no texto dos links.
    """
    for a in soup.find_all("a"):
        if any(termo.lower() in a.text.lower() for termo in termos):
            return 1
    return 0


def encontrar_rede_social(soup: BeautifulSoup, termo: str) -> str:
    """
    Retorna o link da rede social se existir.
    """
    link = soup.find("a", href=lambda href: href and termo in href.lower())
    return link["href"] if link else ""


def analisar_sites(municipios: list[str], urls: list[str]) -> pd.DataFrame:
    """
    Analisa os sites das Câmaras Municipais e retorna um DataFrame consolidado.
    """

    resultados = []

    for municipio, url in zip(municipios, urls):
        dados = {
            "Municipio": municipio,
            "URL": url,
            "Organograma": "",
            "Informações sobre Parlamentares": "",
            "Legislação": "",
            "Notícias sobre a Casa": "",
            "Sessões Remotas": "",
            "Covid-19": "",
            "Ouvidoria": "",
            "Contato": "",
            "Kit mídia": "",
            "Canal especifico de participação": "",
            "Portal da Transparência": "",
            "Facebook": "",
            "Instagram": "",
            "Twitter": "",
            "YouTube": ""
        }

        soup = acessar_site(url)

        if soup is None:
            for chave in dados:
                if chave not in ["Municipio", "URL"]:
                    dados[chave] = "Não disponível"
            resultados.append(dados)
            continue

        dados["Facebook"] = encontrar_rede_social(soup, "facebook")
        dados["Instagram"] = encontrar_rede_social(soup, "instagram")
        dados["Twitter"] = encontrar_rede_social(soup, "twitter")
        dados["YouTube"] = encontrar_rede_social(soup, "youtube")

        dados["Organograma"] = existe_texto(
            soup, ["organograma", "organizacional", "estrutura administrativa"]
        )

        dados["Portal da Transparência"] = existe_texto(
            soup, ["transp"]
        )

        dados["Informações sobre Parlamentares"] = existe_texto(
            soup, ["vereadores", "parlamentares"]
        )

        dados["Legislação"] = existe_texto(
            soup, ["legislação"]
        )

        dados["Notícias sobre a Casa"] = existe_texto(
            soup, ["notícia", "notícias"]
        )

        dados["Sessões Remotas"] = existe_texto(
            soup, ["remotas"]
        )

        dados["Ouvidoria"] = existe_texto(
            soup, ["ouvidoria"]
        )

        dados["Contato"] = existe_texto(
            soup, ["contato", "fone", "telefone", "email"]
        )

        dados["Kit mídia"] = 1 if dados["Facebook"] else 0

        dados["Canal especifico de participação"] = existe_texto(
            soup, ["participação"]
        )

        dados["Covid-19"] = existe_texto(
            soup, ["covid"]
        )

        resultados.append(dados)
        time.sleep(1)

    return pd.DataFrame(resultados)


def salvar_excel(df: pd.DataFrame):
    os.makedirs("data", exist_ok=True)
    caminho = "data/analise_sites_camaras.xlsx"
    df.to_excel(caminho, index=False)
    print(f"Arquivo salvo em: {caminho}")


if __name__ == "__main__":

    urls = []
    municipios = []

    df_resultado = analisar_sites(municipios, urls)
    salvar_excel(df_resultado)
