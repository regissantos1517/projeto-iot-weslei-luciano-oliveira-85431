# pipeline.py

import pandas as pd
from sqlalchemy import create_engine, text
import os

# --- 1. Conexão com o banco de dados ---
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'sua_senha')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USER = os.getenv('DB_USER', 'postgres')

try:
    engine = create_engine(f'postgresql://{DB_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:5432/{DB_NAME}')
    print("Conexão com o banco de dados estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar com o banco de dados: {e}")
    exit()

# --- 2. Criação da tabela (se não existir) ---
def create_table():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS temperature_readings (
                id SERIAL PRIMARY KEY,
                device_id VARCHAR(50) NOT NULL,
                temperature NUMERIC(5, 2) NOT NULL,
                timestamp TIMESTAMP NOT NULL
            );
        """))
        conn.commit()
    print("Tabela 'temperature_readings' verificada/criada com sucesso.")

# --- 3. Ingestão e processamento de dados do CSV ---
def ingest_data(file_path):
    try:
        # Carregar o arquivo CSV
        df = pd.read_csv(file_path)
        print(f"Dados do CSV carregados com sucesso! {len(df)} linhas encontradas.")

        if df.empty:
            print("Erro: O arquivo CSV parece estar vazio.")
            return

        # Renomear as colunas do CSV para o padrão do banco de dados
        df.rename(columns={
            'room_id/id': 'device_id',
            'temp': 'temperature',
            'noted_date': 'timestamp'
        }, inplace=True)
        
        required_columns = ['device_id', 'temperature', 'timestamp']
        if not all(col in df.columns for col in required_columns):
            print("Erro: As colunas esperadas ('room_id/id', 'temp', 'noted_date') não foram encontradas no arquivo CSV.")
            return

        # Preparar os dados para inserção
        df_to_insert = df[required_columns].copy()
        
        # CORREÇÃO APLICADA AQUI: Adicionado dayfirst=True para interpretar o formato da data corretamente
        df_to_insert['timestamp'] = pd.to_datetime(df_to_insert['timestamp'], dayfirst=True)

        # Inserir os dados no banco de dados
        df_to_insert.to_sql('temperature_readings', engine, if_exists='append', index=False)
        print(f"{len(df_to_insert)} linhas de dados inseridas no PostgreSQL com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado. Verifique o caminho.")
    except Exception as e:
        print(f"Erro durante a ingestão dos dados: {e}")

if __name__ == "__main__":
    csv_file_path = os.path.join('data', 'temperature_readings.csv')

    create_table()
    ingest_data(csv_file_path)

