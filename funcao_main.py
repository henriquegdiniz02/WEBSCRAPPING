import requests
from bs4 import BeautifulSoup


def buscar_strings_no_site(
    url: str,
    termos: list[str],
    timeout: int = 10
) -> int:
    """
    Acessa um site e verifica se algum dos termos informados
    aparece no texto de links (<a>).

    Retorna:
    1 -> se encontrar ao menos um termo
    0 -> se não encontrar ou ocorrer erro
    """

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.find_all("a"):
            texto = a.get_text(strip=True).lower()
            if any(termo.lower() in texto for termo in termos):
                return 1

        return 0

    except Exception:
        return 0
