# Usar uma imagem base Python
FROM python:3.9-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto dos arquivos do projeto
COPY . .

# Expor a porta que o Streamlit usa por padrão
EXPOSE 8501

# Comando para executar a aplicação Streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"] 