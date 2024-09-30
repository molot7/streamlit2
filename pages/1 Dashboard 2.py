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

option=st.sidebar.selectbox("Selecciona la variable categórica", categoricas,index=1)

option2=st.sidebar.selectbox("Selecciona la variable numérica", numericas)


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
    tabla = pd.DataFrame({str(option):pd.Series(df[option].unique()), 'Registros':pd.Series(df[option].value_counts().values)})

    st.dataframe(tabla,hide_index=True)

#pone grafico de barras
with col2:

    #st.write("valores anuales")
    fig = go.Figure(data=[
    go.Bar(x=pd.Series(df[option].unique()), y=pd.Series(df[option].value_counts().values), marker_color='royalblue') ])

    fig.update_layout(
    title='Valores anuales',
    xaxis_title=option,
    yaxis_title='Ordenes',
    width=800,   # Ancho del gráfico en píxeles
    height=400,
    xaxis=dict(
        tickangle=90      # Girar las etiquetas del eje X 45 grados en sentido antihorario
    ))
    #template='plotly_white'  # Puedes elegir un tema diferente si lo prefieres)
    st.plotly_chart(fig, theme=None,use_container_width=True)
    #st.plotly_chart(fig, theme=None, use_container_width=True)


#pone grafico de pie
#with col3:
#    fig = go.Figure(data=[go.Pie(labels=pd.Series(df[option].unique()), values=pd.Series(df[option].value_counts().values))])
#    st.plotly_chart(fig, theme=None,use_container_width=True)

st.divider()

st.write("# Datos numéricos")

col1, col2 = st.columns([1,2])

with col1:
    tabla = pd.DataFrame({'Valores':pd.Series(df[option2].unique()), 'Registros':pd.Series(df[option2].value_counts().values)})

    st.dataframe(tabla,hide_index=True)

#pone grafico de barras
with col2:

    #st.write("valores anuales")
    fig = go.Figure(data=[
    go.Bar(x=pd.Series(df[option2].unique()), y=pd.Series(df[option2].value_counts().values), marker_color='royalblue') ])

    fig.update_layout(
    title='Valores anuales',
    xaxis_title=option2,
    yaxis_title='Ordenes',
    width=800,   # Ancho del gráfico en píxeles
    height=400,
    xaxis=dict(
        tickangle=90      # Girar las etiquetas del eje X 45 grados en sentido antihorario
    ))
    #template='plotly_white'  # Puedes elegir un tema diferente si lo prefieres)
    st.plotly_chart(fig, theme=None,use_container_width=True)
    #st.plotly_chart(fig, theme=None, use_container_width=True)