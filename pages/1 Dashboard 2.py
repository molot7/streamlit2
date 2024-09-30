import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
 
st.set_page_config(page_title="pagina 2",layout="wide")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 38px;  /* Ajusta el padding superior según sea necesario */
        padding-left: 10px; /* Ajusta el padding izquierdo según sea necesario */
        padding-right: 20px; /* Ajusta el padding derecho según sea necesario */
        padding-bottom: 0px; /* Ajusta el padding inferior según sea necesario */
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.write("# Exploracion de datos categóricos y numéricos")
#st.write("# Datos categóricos")

df = pd.read_csv('Forbes2.csv')

categoricas=df.columns[df.dtypes=="O"]
numericas=df.select_dtypes(include=['number']).columns

st.sidebar.write("#### controla la primera grafica")

option=st.sidebar.selectbox("Selecciona la variable categórica", categoricas,index=1)

option2=st.sidebar.selectbox("Selecciona la variable numérica", numericas)

st.sidebar.write("#### Para ver el histograma de:")
option3=st.sidebar.selectbox("Selecciona alguna numérica", numericas)


bo = go.Figure()

def box(x,y):
    for i in df[x].unique():
        bo.add_trace(go.Violin(x=df[x][df[x] == i],
                            y=df[y][df[x] == i],
                            name=i,
                            box_visible=True,
                            meanline_visible=True))
        bo.update_layout(title='Grafico de violinplot',
                  yaxis_title=y)
        
        bo.update_layout(height=400)

        bo.update_layout(
                margin=dict(l=60, r=40, t=40, b=100),  # Ajustar márgenes si es necesario
                modebar=dict(
                orientation='h',  # Orientación vertical
                )
                )

    st.plotly_chart(bo,theme=None)
    
box(option,option2)


#numericas=df.select_dtypes(include=['number']).columns
#todas=df.columns
#variables={'Categoricas':categoricas,'Numericas':numericas,'Todas':todas}

#option=st.sidebar.selectbox("Selecciona la variable categorica", ['Atendió', 'Tipo', 'Producto', 'Categoria','Tipo_de_Cliente'])

col1, col2 = st.columns([1,2])

    
#pone una tabla
with col1:
        c1, c2 = st.columns(2)

        c1.container(border=True).metric('Valor promedio de '+str(option3), round((df[option3]).mean(),2), label_visibility="visible")  
        c2.container(border=True).metric('Desviación estandar de '+str(option3), round((df[option3]).std(),2), label_visibility="visible")

#pone grafico de barras
with col2:

    #st.write("valores anuales")
    hist = go.Figure(data=[go.Histogram(x=df[option3])])
    hist.update_layout(
            margin=dict(l=60, r=40, t=40, b=100),  # Ajustar márgenes si es necesario
            modebar=dict(
            orientation='h',  # Orientación vertical
            bgcolor='rgba(255, 255, 255, 0.9)'  # Fondo semi-transparente
                )
                )
    bo.update_layout(height=400)

    hist.update_layout(title_text='Histograma de '+str(option3)+'  (valores globales)')
    #template='plotly_white'  # Puedes elegir un tema diferente si lo prefieres)
    st.plotly_chart(hist, theme=None,use_container_width=True)
    #st.plotly_chart(fig, theme=None, use_container_width=True)


#pone grafico de pie
#with col3:
#    fig = go.Figure(data=[go.Pie(labels=pd.Series(df[option].unique()), values=pd.Series(df[option].value_counts().values))])
#    st.plotly_chart(fig, theme=None,use_container_width=True)

st.divider()