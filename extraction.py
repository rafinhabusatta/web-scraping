import os
import pandas as pd

def save_to_excel(movies_data, file_name="movies.xlsx"):
  # Verificar se o arquivo já existe
  file_exists = os.path.exists(file_name)

  # Criar um DataFrame a partir dos dados
  df = pd.DataFrame(movies_data)

  # Verificar se o arquivo já existe
  if file_exists:
    # Carregar o arquivo existente
    existing_df = pd.read_excel(file_name)
    
    # Concatenar os DataFrames
    df = pd.concat([existing_df, df], ignore_index=True)
    with pd.ExcelWriter(file_name) as writer:
      df.to_excel(writer, index=False)

  else:
    # Salvar os dados em um arquivo Excel
    df.to_excel(file_name, index=False)
  print("Dados salvos no arquivo movies.xlsx")