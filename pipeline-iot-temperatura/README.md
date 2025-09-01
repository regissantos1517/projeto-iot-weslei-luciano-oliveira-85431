Pipeline de Dados com IoT e Docker: Análise de Leituras de Temperatura

1\. Visão Geral do Projeto

Este projeto demonstra a construção de um pipeline de dados completo e moderno para processar, armazenar e visualizar leituras de temperatura de dispositivos IoT. Utilizando um conjunto de dados com quase 100.000 registros, a solução simula um cenário real de monitoramento, transformando dados brutos em insights visuais e acionáveis através de um dashboard interativo.



A arquitetura foi projetada para ser robusta, escalável e facilmente replicável, utilizando tecnologias de ponta como Docker, PostgreSQL, Python e Streamlit.



2\. Visualização Final: Dashboard Interativo

O resultado final do projeto é um dashboard interativo que apresenta três análises principais sobre os dados dos sensores:



Gráfico 1: Média de Temperatura por Dispositivo



Gráfico 2: Leituras de Temperatura por Hora do Dia



Gráfico 3: Variação Diária de Temperaturas Máxima e Mínima



3\. Tecnologias Utilizadas

Linguagem de Programação: Python 3.x



Banco de Dados: PostgreSQL (executando em um contêiner Docker)



Conteinerização: Docker e Docker Compose



Bibliotecas Python:



Pandas: Para manipulação e limpeza dos dados.



SQLAlchemy: Para a conexão e comunicação com o banco de dados PostgreSQL.



Psycopg2-binary: Driver de conexão PostgreSQL para Python.



Streamlit: Para a construção do dashboard web interativo.



Plotly Express: Para a criação dos gráficos interativos.



Conjunto de Dados: Temperature Readings: IoT Devices (Kaggle)



4\. Estrutura do Projeto

O repositório está organizado da seguinte forma para garantir a clareza e a modularidade do código:



.

├── src/

│   ├── pipeline.py         # Script para ingestão e ETL dos dados

│   └── dashboard.py        # Script do dashboard Streamlit

├── data/

│   └── temperature\_readings.csv  # Conjunto de dados original

├── sql/

│   └── create\_views.sql    # Script SQL para criação das views no banco

├── docs/

│   └── Parte\_Teorica\_IOT.pdf   # Documentação teórica completa do projeto

├── .gitignore

├── requirements.txt        # Lista de dependências Python

└── docker-compose.yml      # Arquivo de configuração dos serviços Docker



5\. Instruções de Instalação e Execução

Para executar este projeto em sua máquina local, siga os passos abaixo.



Pré-requisitos

Git



Docker Desktop



Python 3.8+



Passo a Passo

1\. Clonar o Repositório:



git clone https://URL\_DO\_SEU\_REPOSITORIO.git

cd nome-do-repositorio



2\. Iniciar o Banco de Dados com Docker:

O docker-compose irá criar e iniciar o contêiner do PostgreSQL em segundo plano.



docker compose up -d



3\. Criar e Ativar um Ambiente Virtual (Recomendado):



\# Criar o ambiente

python -m venv venv



\# Ativar no Windows

.\\venv\\Scripts\\activate



\# Ativar no macOS/Linux

source venv/bin/activate



4\. Instalar as Dependências:



pip install -r requirements.txt



5\. Executar o Pipeline de Ingestão de Dados:

Este script irá popular o banco de dados com os dados do arquivo CSV.



python src/pipeline.py



6\. Criar as Views no Banco de Dados (Manualmente):

Conecte-se ao contêiner e execute o script SQL.



\# Conectar ao psql

docker exec -it postgres-iot psql -U postgres



\# No console psql (postgres=#), cole o conteúdo do arquivo 'sql/create\_views.sql' e pressione Enter.

\# Depois, saia com o comando \\q



7\. Executar o Dashboard:

Este comando iniciará a aplicação Streamlit e a abrirá no seu navegador.



streamlit run src/dashboard.py



6\. Autor

Weslei Luciano de Sousa Oliveira



RA: 85431

