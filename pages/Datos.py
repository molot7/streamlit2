import streamlit as st
import pandas as pd


#nobre pagina e icono
st.set_page_config(page_title="Hello",page_icon="👋",layout="wide")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 13px;  /* Ajusta el padding superior según sea necesario */
        padding-left: 10px; /* Ajusta el padding izquierdo según sea necesario */
        padding-right: 20px; /* Ajusta el padding derecho según sea necesario */
        padding-bottom: 10px; /* Ajusta el padding inferior según sea necesario */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("### Creado por Diego para perfil de OCC")

#df = pd.read_csv('apartments.csv', delimiter=';',encoding='latin1')# el df es temporal luego se sustituira por el archivo subido
df = pd.read_csv('Forbes2.csv')


st.write("#### Exploracion de los datos")
st.dataframe(df.head(200),hide_index=True)


c1, c2,c3,c4 = st.columns(4)

c1.container(border=True).metric('Cantidad de filas',df.shape[0] , delta_color="normal", label_visibility="visible")  
c2.container(border=True).metric('Número de variables', df.shape[1], delta_color="normal", label_visibility="visible") 
c3.container(border=True).metric('Número de variables categoricas', len(df.columns[df.dtypes=="O"]), delta_color="normal", label_visibility="visible")
c4.container(border=True).metric('Número de variables numéricas', len(df.select_dtypes(include=['number']).columns), delta_color="normal", label_visibility="visible")

nul=df.isnull().sum()
nulos=pd.DataFrame({'datos nulos por columna':nul})

st.dataframe(nulos,hide_index=False)





