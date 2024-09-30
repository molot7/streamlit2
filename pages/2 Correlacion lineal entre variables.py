import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

 
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 18px;  /* Ajusta el padding superior según sea necesario */
        padding-left: 10px; /* Ajusta el padding izquierdo según sea necesario */
        padding-right: 20px; /* Ajusta el padding derecho según sea necesario */
        padding-bottom: 10px; /* Ajusta el padding inferior según sea necesario */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("## Correlacion lineal entre variables numéricas")
#forbes
df = pd.read_csv('Forbes2.csv')

numericas=df.select_dtypes(include=['number']).columns



col1, col2= st.columns([1,2])

with col1:
    matriz = df[numericas].corr()
    fig1 = px.imshow(matriz,
                text_auto=True, 
                title='Matriz de Correlación',
                color_continuous_scale='RdBu',  
                width=800,  # Ajusta el ancho
                height=600)
    
    fig1.update_layout(
            margin=dict(l=60, r=40, t=40, b=100),  # Ajustar márgenes si es necesario
            modebar=dict(
            orientation='h',  # Orientación vertical
            bgcolor='rgba(255, 255, 255, 0.9)'  # Fondo semi-transparente
                )
                )
    
    st.plotly_chart(fig1, theme=None,use_container_width=True)

  
    
    #option2=st.selectbox("Mostrar por Orden",('Todas','Categoricas','Numericas')
    
    
with col2:

    mdis = px.scatter_matrix(df[numericas],title="Matriz de Dispersión")
    st.plotly_chart(mdis, theme=None,use_container_width=True)
    
    

