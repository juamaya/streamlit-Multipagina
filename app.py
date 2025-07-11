import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image


st.set_page_config(
    page_title="Juamaya Website",
    page_icon="🔥",
    layout="centered"
)

def pagina_principal():
 

    st.title("Pagina Principal")
    st.markdown(" # My first app con streamlit" )
    img = Image.open("streamlit.jpg")
    st.image(img )
    st.write(4 + 6)
    st.success("## Bienvenido a la Aplicacion")
  
    st.image("https://picsum.photos/800", width= 400)

    st.warning("### Registros 74HC595 en cascada._Datos serie-paralelo")
    with open ("video1.mp4", "rb") as video_file:
        st.video(video_file.read(), start_time=0 )
    st.markdown('Juamaya 🍺 2025')
############################################################
def visualizar_Datos():
    st.title("Visualizacion de Datos")
    st.info("Carga un archivo CSV para visualizar los datos") 
    archivo_cargado = st.file_uploader(" Elige un archivo CSV", type="csv")   

    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Datos del archivo CSV")
        st.write(df)
        st.write("Estadisticas Descriptivas")
        st.write(df.describe())
        st.write(df.head())
        st.write(df.tail())
        st.header("Dataframe")
        df2 = df.sample(n=10, random_state=13)
        st.dataframe(df2.style.highlight_max(axis=0))

        st.markdown('Juamaya 🍺 2025')
############################################################

def graficos_interactivos():
    st.title("Graficos Interactivos")
    st.info("Carga un archivo CSV para crear Graficos Interactivos") 
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv", key="2")  
    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Elige una columna para el eje X") 
        eje_x = st.selectbox ("Eje X", df.columns)
        st.write("Elige una columna para el eje Y") 
        eje_y = st.selectbox ("Eje Y", df.columns)

        if st.button("Crear Grafico"):
            fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)
        st.markdown('Juamaya 🍺 2025')
############################################################
def curso_streamlit():
       st.success("## Tutorial de Streamlit")
       img = Image.open("streamlit.jpg")
       st.image(img )
       st.info("#### Streamlit es un Framework de Python para crear paginas Web.")

       st.title("Esto es un Titulo")
       st.header(" Esto en encabezado")
       st.subheader(" Esto en sub encabezado")
       st.write("Texto Normal")

       name="Juan"
       st.text(f"Hola {name} Esto es un texto")
       st.markdown("## Esto es un markdown")

       st.title("Archivo .json")
       st.json({"clave":"valor","clave1":"valor1","clave2":"valor2",})



       st.title("Mensajes")
       st.success("EXITO")
       st.info("INFORMACION")
       st.warning("ADVERTENCIA")
       st.error("ERROR")


       st.title("Codigos")

       codigo ="""
       def saludar():
           print ("Hola")
       """
       st.code(codigo, language="python")

       st.title("Selectbox")
       opcion = st.selectbox("Elige tu fruta favorita", ["Pera","Naranja","Platano","Fresa"])
       st.write("### Tu fruta favorita es :" , opcion)

       opciones = st.multiselect("Elige tus colores favoritos", ["Rojo","Naranja","Verde","Negro","Banco","Azul"])
       st.write(f"#### Tus colores favoritos son : {opciones}"  )


       st.title("Slider")
       edad = st.slider("Selecciona tu edad", 
                        min_value =0,
                        max_value=100,
                        value=25,step=1
                        )
       st.write("### Tu edad es :" , edad ," años")

       st.title("Imagenes")
       img = Image.open("streamlit.jpg")
       st.image(img )

       st.title("Videos")
       st.warning("## Registros 74HC595 en cascada ")
       with open ("video1.mp4", "rb") as video_file:
          st.video(video_file.read(), start_time=0 )

       st.title("Entrada de datos")

       nombre = st.text_input("Ingresa tu nombre")
       st.write("Tu nombre es:", nombre)
       mensaje = st.text_area("Ingresa tu mensaje", height=100)
       st.write("Tu mensaje es:", mensaje)
       numero = st.number_input("Ingresa un numero", 1.0, 25.0, step=1.0 )
       st.write("Tu numero es:",numero)
       fecha = st.date_input("Selecciona una fecha"  )
       st.write("Tu fecha es:",fecha)
       hora = st.time_input("Selecciona una hora"  )
       st.write("Tu hora es:",hora)
       color = st.color_picker("Selecciona un color "  )
       st.write("El codigo hexagesimal de tu color es: ", color)
       st.markdown('Juamaya 🍺 2025')
############################################################

st.sidebar.title("Navegacion")

pagina= st.sidebar.selectbox("Selecione una pagina", ["Pagina Principal", "Visualizacion de Datos","Graficos Interactivos", "Tutorial de Streamlit"])

if pagina == "Pagina Principal":
    pagina_principal()
elif pagina == "Visualizacion de Datos":
    visualizar_Datos()
elif pagina == "Graficos Interactivos":
    graficos_interactivos()
elif pagina == "Tutorial de Streamlit":
   curso_streamlit()   