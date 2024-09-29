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


bo = go.Figure()

def box(x,y):
    for i in df[x].unique():
        bo.add_trace(go.Violin(x=df[x][df[x] == i],
                            y=df[y][df[x] == i],
                            fillcolor='rgba(0, 255, 0, 0.5)',
                            name=i,
                            box_visible=True,
                            meanline_visible=True))
        bo.update_layout(title='Grafico de violinplot',
                  yaxis_title=y,
                  xaxis_title=i)

    st.plotly_chart(bo,theme=None)
    
box(option,option2)

def barras (x,y):
        grouped_df = df.groupby(x, as_index=False).sum()

        fig2 = go.Figure([go.Bar(x=df[x].unique(), y=df[y])])
        fig2.update_layout(
        title='Gráfico violinplot',
        xaxis_title=str(x),
        yaxis_title=str(y),
        template='plotly_white'
        )

        st.plotly_chart(fig2,theme=None)



barras (option,option2)



col1, col2= st.columns([1,1])

with col1:
        grouped_df = df.groupby(option, as_index=False).sum()
        st.dataframe(grouped_df[list([option]) + list(numericas)],hide_index=True)


    
    
with col2:
        fig = go.Figure(data=[go.Pie(labels=pd.Series(df[option].unique()), values=df.groupby(option, as_index=False).sum()[option2])])
        st.plotly_chart(fig, theme=None,use_container_width=True)

        #st.plotly_chart(fig, theme=None, use_container_width=True)


