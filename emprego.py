import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carrega o arquivo Excel
@st.cache
def load_data(file):
    df = pd.read_excel(file)
    return df

# Função para plotar o gráfico
def plot_graph(data, selected_job):
    filtered_data = data[data['Vaga'] == selected_job]
    if not filtered_data.empty:
        plt.figure(figsize=(10, 6))
        plt.hist(filtered_data['Salário'], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Distribuição de Salários para a vaga de {selected_job}')
        plt.xlabel('Salário')
        plt.ylabel('Frequência')
        st.pyplot()
    else:
        st.write(f'Não há dados disponíveis para a vaga de {selected_job}')

def main():
    st.title('Análise de Salários por Cargo')

    # Carrega os dados
    file = st.file_uploader("Carregar arquivo Excel", type=['xlsx'])
    if file is not None:
        data = load_data(file)
        job_list = data['Vaga'].unique()

        # Seleciona o cargo
        selected_job = st.selectbox('Selecione o cargo:', job_list)

        # Mostra o gráfico
        plot_graph(data, selected_job)

if __name__ == "__main__":
    main()
