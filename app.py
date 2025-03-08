import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Análise de Reclamações", layout="wide")
st.title("Dashboard de Reclamações - 2017")

# Carregar dados


@st.cache_data
def load_data():
    return pd.read_csv('data/base reclamações.csv', sep=';', encoding='latin-1')


df = load_data()

# Tratar dados
df['empresa'] = df['empresa'].fillna('Nao Informada')
df['estado'] = df['estado'].fillna('Nao Informada')
df['serviço'] = df['serviço'].fillna('Nao Informada')

# Sidebar
st.sidebar.header("Filtros")
selected_analysis = st.sidebar.selectbox(
    "Selecione a Análise", ["Empresas", "Estados", "Serviços"])

# Função para exibir wordcloud


def display_wordcloud(data, title):
    wordcloud = WordCloud(
        width=800, height=400, background_color='white').generate_from_frequencies(data)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title(title)
    st.pyplot(fig)


# Exibir análise selecionada
if selected_analysis == "Empresas":
    st.subheader("Top 10 Empresas com Mais Reclamações")
    top_empresas = df['empresa'].value_counts().head(10)
    st.bar_chart(top_empresas)
    display_wordcloud(df['empresa'].value_counts().to_dict(),
                      "Wordcloud de Empresas")

elif selected_analysis == "Estados":
    st.subheader("Top 10 Estados com Mais Reclamações")
    top_estados = df['estado'].value_counts().head(10)
    st.bar_chart(top_estados)
    display_wordcloud(df['estado'].value_counts().to_dict(),
                      "Wordcloud de Estados")

elif selected_analysis == "Serviços":
    st.subheader("Top 10 Serviços com Mais Reclamações")
    top_servicos = df['serviço'].value_counts().head(10)
    st.bar_chart(top_servicos)
    display_wordcloud(df['serviço'].value_counts().to_dict(),
                      "Wordcloud de Serviços")
