from sheet import get_movie_names_from_excel
from search import search_imdb
from extraction import save_to_excel

def main(excel_file_path):
    # Obter os filmes da planilha exportada
    movie_names = get_movie_names_from_excel(excel_file_path)
    results = []

    user_input = input("Digite o número máximo de resultados por busca (digite -1 ou pressione enter para salvar todos): ")
    if user_input == "":
        max_results = -1
    else:
        # Tentar converter o valor digitado para um número inteiro
        try:
            max_results = int(user_input)
        except ValueError:
            # Caso não seja um número válido, podemos definir o valor padrão
            print("Valor inválido, todos os resultados serão salvos para cada busca")
            max_results = -1

    # Para cada filme, realizar a pesquisa no IMDb
    for movie_name in movie_names:
        print(f"Pesquisando: {movie_name}")
        search_results = search_imdb(movie_name, max_results)
        results.extend(search_results)

    # Salvar os resultados em um arquivo Excel
    save_to_excel(results, "movies.xlsx")

if __name__ == "__main__":
    excel_file_path = "movie_list.xlsx"  # Altere para o caminho do seu arquivo
    main(excel_file_path)