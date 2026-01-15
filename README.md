# Democracia e Comunicação Digital  
## Web Scraping de Sites de Câmaras Municipais Brasileiras

Este repositório reúne scripts em Python para **coleta, identificação e análise de sites de Câmaras Municipais no Brasil**, com foco na **presença digital institucional**, transparência e canais de comunicação pública.

O projeto utiliza **web scraping** e **APIs públicas** para estruturar uma base de dados que permita análises sobre **democracia digital, comunicação institucional e acesso à informação** no nível municipal.

## Funcionalidades

- Coleta automática de municípios via **API do IBGE**
- Identificação dos sites oficiais das Câmaras Municipais
- Raspagem de dados dos sites institucionais
- Verificação da presença de conteúdos como:
  - Organograma
  - Informações sobre parlamentares
  - Legislação
  - Notícias institucionais
  - Portal da Transparência
  - Ouvidoria e canais de contato
  - Canais de participação cidadã
- Mapeamento de redes sociais institucionais
- Exportação dos resultados para arquivos Excel

## Tecnologias Utilizadas

- Python 3
- Requests
- BeautifulSoup
- Pandas
- Google Custom Search API
- API do IBGE

## Estrutura do Repositório

```text
democracia-comunicacao-digital/
│
├── src/
│   ├── ibge_populacao.py          # Coleta de municípios via API do IBGE
│   ├── coleta_links_camaras.py    # Busca dos sites das Câmaras
|   ├── funcao_main.py             # Função generica para ser usada com qualquer string
│   └── analise_sites_camaras.py   # Raspagem e análise dos sites
│
│
└── README.md
