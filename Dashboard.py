import streamlit as st
import pandas as pd
import plotly.graph_objects as go


 
st.set_page_config(page_title="pagina 2",layout="wide")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 20px;  /* Ajusta el padding superior según sea necesario */
        padding-left: 10px; /* Ajusta el padding izquierdo según sea necesario */
        padding-right: 20px; /* Ajusta el padding derecho según sea necesario */
        padding-bottom: 10px; /* Ajusta el padding inferior según sea necesario */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("## Ejemplo de dashboard en streamlit")

df = pd.read_csv('Forbes2.csv')

categoricas=df.columns[df.dtypes=="O"]
numericas=df.select_dtypes(include=['number']).columns

option=st.sidebar.selectbox("Agrupar por variable categpórica", categoricas,index=1)
option2=st.sidebar.selectbox("Selecciona la variable numérica", numericas)

#options = st.sidebar.multiselect(
 #   "What are your favorite colors",
 #   categoricas,'Company')

grouped_df = df.groupby(option, as_index=False).sum()

fig2 = go.Figure([go.Bar(x=df[option].unique(), y=df[option2])])
fig2.update_layout(
        title='Gráfico de Barras',
        xaxis_title=str(option),
        yaxis_title=str(option2),
        template='plotly_white'
        )

st.plotly_chart(fig2,theme=None)

col1, col2= st.columns([1,1])

with col1:
        st.dataframe(grouped_df[list([option]) + list(numericas)],hide_index=True)


    
    
with col2:
        fig = go.Figure(data=[go.Pie(labels=pd.Series(df[option].unique()), values=df.groupby(option, as_index=False).sum()[option2])])
        st.plotly_chart(fig, theme=None,use_container_width=True)

        #st.plotly_chart(fig, theme=None, use_container_width=True)


