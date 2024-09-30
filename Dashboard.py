import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np  
import random
import plotly.express as px
 
st.set_page_config(page_title="pagina 1",layout="wide")
# Estilo CSS para cambiar el color de fondo


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

st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #d9d9d9;  /* Color gris más oscuro */
    }
    .sidebar .sidebar-content {
        background-color: #d9d9d9;  /* Asegúrate de que la barra lateral también tenga el mismo color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.write("### Ejemplo de dashboard dinámico interactivo en streamlit para Vanquish,  creado por Diego")

df = pd.read_csv('Forbes2.csv')

categoricas=df.columns[df.dtypes=="O"]
numericas=df.select_dtypes(include=['number']).columns

option=st.sidebar.selectbox("Agrupar por variable categpórica", categoricas,index=1)
option2=st.sidebar.selectbox("Selecciona la variable numérica", numericas)

def generar_colores_hex(n):
    color = ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(n)]
    return color

# Ejemplo: generar 10 colores
colores = generar_colores_hex(80)
#colores = ['#'+''.join([np.random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(len(categoricas))]

#options = st.sidebar.multiselect(
 #   "What are your favorite colors",
 #   categoricas,'Company')




col1, col2, col3= st.columns([0.8,0.5,2])

with col1:
        grouped_df = df.groupby(option, as_index=False).sum().sort_values(by=option2,ascending=False)
        st.write("##### solo se muestran las primeras 5 filas")
        st.dataframe(grouped_df[list([option]) + list([option2])].head(5),hide_index=True)

with col2:
      container = st.container(border=True,height=90)
      container.metric('Valor maximo de '+str(option2), max(grouped_df[option2]), label_visibility="visible")
      #st
      container = st.container(border=True,height=90)
      container.metric('Valor promedio de '+str(option2), round((grouped_df[option2]).mean(),2))

      container = st.container(border=True,height=90)
      container.metric('Valor minimo de '+str(option2), min(grouped_df[option2]))
    
with col3:
    def barras (x,y):
            
            grouped_df = df.groupby(x, as_index=False).sum().sort_values(by=y,ascending=False)

            fig2 = go.Figure([go.Bar(x=df[x].unique(), y=grouped_df[y],marker_color=colores)])
            fig2.update_layout(
            title=str(x),
            
            yaxis_title='Suma de ' +str(y)+' (USD)')

            fig2.update_layout(height=400)

            fig2.update_layout(
            margin=dict(l=60, r=40, t=40, b=100),  # Ajustar márgenes si es necesario
            modebar=dict(
            orientation='h',  # Orientación vertical
            bgcolor='rgba(255, 255, 255, 0.9)'  # Fondo semi-transparente
                )
                )

            return fig2

    with st.container():
        st.plotly_chart(barras(option,option2),theme=None)
        
       
    #st.write("## Ejemplo de dashboard en streamlit")
dgeo = pd.read_csv('datosgeo.csv')
#para los pises

col3, col4= st.columns([1,1])

with col3:
        def pais(val):
        # Crear elgráfico
            geo = go.Figure(data=go.Choropleth(
                locations=grouped_df['Country'],          # Países
                locationmode='country names',    # Modo de ubicación
                z=grouped_df[val],                 # Valores para la coloración
                colorscale='Viridis',            # Escala de color variada
                colorbar=dict(title=str(option2)+' (USD)'),    # Título de la barra de color
            ))
    
    # Ajustar el layout para el mapa esférico
            geo.update_geos(
                projection_type='orthographic',   # Proyección esférica
                showland=True,
                landcolor='rgba(255, 255, 255, 0.1)',  # Color de la tierra
                countrycolor='rgba(200, 200, 200, 0.5)',  # Color de las fronteras
                 bgcolor='rgba(173, 216, 230, 0.5)'  # Fondo azul claro
            )
            geo.update_layout(
            margin=dict(l=60, r=40, t=40, b=100),  # Ajustar márgenes si es necesario
            modebar=dict(
            orientation='h',  # Orientación vertical
                )
                )
    
                # Añadir título
            geo.update_layout(title_text='Mapa esférico interactivo de '+str(val)+' total por país')
            st.plotly_chart(geo,theme=None)

        def conti(val):
            continent_values = df.groupby(['Continent','Country']).agg({val: 'sum'}).reset_index()
            p=['EGY','MUS','MAR','NGA','ZAF','TGO','BHR','CHN','HKG','IND','IDN','ISR','JPN','JOR','KAZ','KWT','LBN','MYS','OMN','PAK','PHL','QAT','RUS','SAU','SGP','KOR','TWN','THA','ARE','VNM','AUS','AUT','BEL','CZE','DNK','FIN','FRA','DEU','GRC',
            'HUN','IRL','ITA','LUX','NLD','NOR','POL','PRT','ESP','SWE','CHE','TUR','GBR','BMU','CAN','CYM','MEX','PRI','USA','BRA','CHL','COL','PER','VEN']
            continent_values['iso']=p

            continent_values[val]=continent_values[val].abs()
    
            geo2=px.scatter_geo(continent_values,locations='iso',color='Continent',hover_name='Country',size=val,projection='orthographic')
            geo2.update_geos(
                projection_type='orthographic',   # Proyección esférica
                showland=True,
                landcolor='rgba(255, 255, 255, 0.1)',  # Color de la tierra
                countrycolor='rgba(200, 200, 200, 0.5)',  # Color de las fronteras
                 bgcolor='rgba(173, 216, 230, 0.5)'  # Fondo azul claro
            )

            geo2.update_layout(
                margin=dict(l=60, r=40, t=40, b=100),  # Ajustar márgenes si es necesario
                modebar=dict(
                orientation='h',  # Orientación vertical
                )
                )
            
            geo2.update_layout(title_text='Mapa esférico interactivo de '+str(val)+' total por continente')
            st.plotly_chart(geo2, theme=None,use_container_width=True)


        if option=='Country':
              pais(option2)


        elif option=='Continent':

              conti(option2)
        
        else:
              st.write("##### Seleccione alguna variable geografica para visualizar mapa aqui")

    # Mostrar el gráfico
        





with col4:
        fig = go.Figure(data=[go.Pie(labels=pd.Series(df[option].unique()), 
                                     values=df.groupby(option, as_index=False).sum()[option2])])
        
        fig.update_layout(
            margin=dict(l=60, r=40, t=40, b=100),  # Ajustar márgenes si es necesario
            modebar=dict(
            orientation='h',  # Orientación vertical
            bgcolor='rgba(255, 255, 255, 0.9)'  # Fondo semi-transparente
                )   
                )
        
        st.plotly_chart(fig, theme=None,use_container_width=True)

        #st.plotly_chart(fig, theme=None, use_container_width=True)


