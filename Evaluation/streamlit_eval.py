import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(0)
df = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'z': np.random.rand(100)
})


chart_type = st.sidebar.selectbox(
    'Sélectionnez le type de graphique',
    ['Graphique à barres', 'Graphique linéaire', 'Nuage de points']
)

columns = st.sidebar.multiselect(
    'Sélectionnez les colonnes',
    df.columns
)

if chart_type == 'Graphique à barres':
    fig, ax = plt.subplots()
    for col in columns:
        ax.bar(df.index, df[col], label=col)
    ax.set_xlabel('Index')
    ax.set_ylabel('Valeurs')
    ax.legend()
    st.pyplot(fig)
elif chart_type == 'Graphique linéaire':
    fig, ax = plt.subplots()
    for col in columns:
        ax.plot(df.index, df[col], label=col)
    ax.set_xlabel('Index')
    ax.set_ylabel('Valeurs')
    ax.legend()
    st.pyplot(fig)
elif chart_type == 'Nuage de points':
    if len(columns) == 2:
        fig, ax = plt.subplots()
        ax.scatter(df[columns[0]], df[columns[1]])
        ax.set_xlabel(columns[0])
        ax.set_ylabel(columns[1])
        st.pyplot(fig)
    else:
        st.error('Veuillez sélectionner exactement deux colonnes pour le nuage de points.')
