import pandas as pd

def get_movie_names_from_excel(file_path):
  # Carregar os dados do excel
  df = pd.read_excel(file_path)
  movie_names = df.iloc[:, 0].dropna().tolist()
  return movie_names