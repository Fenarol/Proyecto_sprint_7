# Proyecto_sprint_7

Proyecto Sprint 7

# Aplicación Web de Análisis de Vehículos en Venta 🚗

Este proyecto es una **aplicación web** construida con **Streamlit**, que permite a los usuarios explorar interactivamente un conjunto de datos de anuncios de venta de vehículos (`vehicles_us.csv`).

## Funcionalidad de la Aplicación

La aplicación ofrece las siguientes funcionalidades:

- **Visualización de Histogramas**:
  - El usuario puede seleccionar cualquier columna numérica del conjunto de datos y construir un histograma interactivo utilizando `Plotly Express`.
- **Visualización de Diagramas de Dispersión**:
  - El usuario puede seleccionar qué variables utilizar para el eje X y el eje Y y crear un gráfico de dispersión interactivo para analizar relaciones entre variables.
- **Vista previa de los datos**:
  - Existe la opción de mostrar las primeras filas del conjunto de datos para exploración inicial.

Todas las gráficas son interactivas, lo que permite acercar, desplazar y seleccionar áreas específicas para analizar.

## Tecnologías utilizadas

- **Python 3**
- **Pandas** para el manejo de datos
- **Plotly Express** para la creación de gráficos interactivos
- **Streamlit** para construir la aplicación web

## Instrucciones para ejecutar el proyecto

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener el archivo `vehicles_us.csv` en la misma carpeta que `app.py`.
3. Instala las dependencias necesarias:

   ```bash
   pip install streamlit pandas plotly
   ```

4. Ejecuta la aplicación web con el siguiente comando:

   streamlit run app.py

5. Se abrirá automáticamente en tu navegador un servidor local mostrando la aplicación.
