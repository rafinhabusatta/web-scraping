import requests
from bs4 import BeautifulSoup

def search_trakt(movie_name):
    # URL de busca no Trakt
    base_url = "https://www.imdb.com/find"
    params = {"q": movie_name,"s": "all"}

    # Fazer a requisição
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Erro ao acessar o Trakt. Código HTTP: {response.status_code}")
        return

    # Parsear o conteúdo HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Procurar os resultados
    results = soup.find_all("li", class_="ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result")
    
    # Verificar se há resultados
    if not results:
        print("Nenhum resultado encontrado ou o layout do site mudou.")
        return

    # Processar os resultados
    for result in results[:5]:  # Exibir apenas os primeiros 5
        # Encontrar o título
        title_element = result.find("a", class_="ipc-metadata-list-summary-item__t")
        title = title_element.text.strip() if title_element else "Título não encontrado"

        # Encontrar o ano
        year_element = result.find("span", class_="ipc-metadata-list-summary-item__li")
        year = year_element.text.strip() if year_element else "Ano desconhecido"

        # Encontrar o link
        link = (
            "https://www.imdb.com" + title_element["href"]
            if title_element and title_element.get("href")
            else "Link indisponível"
        )

        # Exibir o resultado
        print(f"Filme: {title} ({year})")
        print(f"Link: {link}")
        print("-" * 30)

# Testar a função
search_trakt("Inception")
