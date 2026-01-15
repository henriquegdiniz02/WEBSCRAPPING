# Democracia e Comunicação Digital
## Análise de Presença Institucional em Sites de Câmaras Municipais

Este projeto tem como objetivo analisar a presença digital e os mecanismos de comunicação institucional das Câmaras Municipais brasileiras, a partir da raspagem automatizada de dados de seus sites oficiais.

A iniciativa insere-se no campo de Democracia e Comunicação Digital, buscando identificar elementos fundamentais de transparência, acesso à informação, participação cidadã e comunicação pública no ambiente digital.

Objetivos do Projeto

Identificar a existência de sites oficiais das Câmaras Municipais

Avaliar a presença de conteúdos institucionais básicos, como:

Organograma

Informações sobre parlamentares

Legislação

Notícias institucionais

Portal da Transparência

Ouvidoria e canais de contato

Canais específicos de participação cidadã

Mapear a presença das Câmaras nas redes sociais

Estruturar uma base de dados padronizada para análises comparativas

Metodologia

O projeto é estruturado em três etapas principais:

1. Coleta de Municípios (IBGE)

Utiliza a API do IBGE para obter a lista de municípios por Unidade da Federação e seus dados populacionais, garantindo padronização territorial e confiabilidade dos dados.

2. Identificação dos Sites Oficiais

Emprega a Google Custom Search API para localizar automaticamente os sites oficiais das Câmaras Municipais a partir do nome do município.

3. Raspagem e Análise dos Sites

Realiza web scraping nos sites identificados para verificar a presença de conteúdos institucionais e canais de comunicação, analisando o HTML das páginas com base na ocorrência de palavras-chave em links e estruturas de navegação.

Tecnologias Utilizadas

Python 3

Requests – requisições HTTP

BeautifulSoup – raspagem e análise de HTML

Pandas – organização e estruturação dos dados

Google Custom Search API – localização dos sites

API do IBGE – dados territoriais oficiais

Estrutura do Repositório
democracia-comunicacao-digital/
│
├── src/
│   ├── ibge_populacao.py          # Coleta de municípios via API do IBGE
│   ├── coleta_links_camaras.py    # Busca dos sites das Câmaras
│   └── analise_sites_camaras.py   # Raspagem e análise dos sites
│
├── data/
│   ├── populacao_municipios.xlsx
│   ├── links_camaras_municipais.xlsx
│   └── analise_sites_camaras.xlsx
│
├── requirements.txt
└── README.md

Lógica Central de Análise

A lógica principal do projeto baseia-se na verificação automatizada da presença de strings específicas nos links dos sites, representando conteúdos institucionais relevantes.

Exemplo de abordagem:

Buscar termos como “Organograma”, “Transparência”, “Vereadores”, “Ouvidoria”, entre outros

Retornar indicadores binários (0 ou 1) para cada dimensão analisada

Essa estratégia permite padronização, escalabilidade e replicabilidade da análise.

Resultados Esperados

Base estruturada com indicadores de presença digital institucional

Possibilidade de criação de índices de transparência e comunicação

Subsídios empíricos para pesquisas sobre:

Democracia digital

Transparência pública

Comunicação institucional no nível municipal

Contexto Acadêmico

Democracia e Comunicação Digital
Realizei a raspagem de dados de sites de câmaras municipais no Brasil, aplicando bibliotecas do Python como BeautifulSoup, Pandas e Requests, com o objetivo de analisar a presença de mecanismos institucionais de transparência, comunicação e participação cidadã no ambiente digital.

Observações Éticas e Técnicas

O scraping respeita intervalos entre requisições para evitar sobrecarga nos servidores

São analisados apenas conteúdos publicamente disponíveis

O projeto não coleta dados pessoais

Possíveis Extensões

Criação de um índice composto de comunicação e transparência

Análise temporal da evolução dos sites

Integração com dados socioeconômicos

Visualizações interativas em dashboards (Power BI / Shiny)
