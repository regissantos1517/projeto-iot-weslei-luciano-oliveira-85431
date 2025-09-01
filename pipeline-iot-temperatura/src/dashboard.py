# dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os

# --- 1. Configuração da Conexão com o Banco de Dados ---
# Utiliza variáveis de ambiente para a senha e outros detalhes de conexão
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'sua_senha')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'postgres')
DB_USER = os.getenv('DB_USER', 'postgres')

try:
    # String de conexão usando SQLAlchemy
    engine = create_engine(f'postgresql://{DB_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:5432/{DB_NAME}')
    print("Conexão com o banco de dados estabelecida com sucesso!")
except Exception as e:
    st.error(f"Erro ao conectar com o banco de dados: {e}")
    st.stop()

# --- 2. Função para carregar dados de uma view ---
@st.cache_data
def load_data(view_name):
    """
    Carrega dados de uma view SQL do PostgreSQL para um DataFrame Pandas.
    A função é otimizada com cache para evitar múltiplas consultas.
    """
    try:
        df = pd.read_sql(f"SELECT * FROM {view_name}", engine)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados da view '{view_name}': {e}")
        return pd.DataFrame()

# --- 3. Título e cabeçalho do Dashboard ---
st.title('Dashboard de Temperaturas IoT')
st.markdown("---")

# --- 4. Visualização 1: Média de temperatura por dispositivo ---
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
if not df_avg_temp.empty:
    fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp',
                  title='Média de Temperatura por Dispositivo')
    st.plotly_chart(fig1)

# --- 5. Visualização 2: Contagem de leituras por hora do dia ---
st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
if not df_leituras_hora.empty:
    # Garante que a coluna 'hora' seja tratada como categórica para a visualização
    df_leituras_hora['hora'] = df_leituras_hora['hora'].astype(str)
    fig2 = px.line(df_leituras_hora, x='hora', y='contagem',
                   title='Contagem de Leituras por Hora do Dia')
    st.plotly_chart(fig2)

# --- 6. Visualização 3: Temperaturas máximas e mínimas por dia ---
st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
if not df_temp_max_min.empty:
    fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'],
                   title='Temperaturas Máximas e Mínimas por Dia')
    st.plotly_chart(fig3)