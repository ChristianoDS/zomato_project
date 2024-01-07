# Libraries

import pandas as pd
import plotly.express as px
import folium
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
import inflection
from folium.plugins import MarkerCluster

#======================================================================================== 
#                              Parâmetros do layout
#========================================================================================
st.set_page_config(page_title='Visão geral',page_icon='🌏',layout='wide')
#========================================================================================
#                           Funções
#========================================================================================
def rename_columns(dataframe):
  ''' Esta função tem por objetivo renomear todas as colunas do dataframe, ajustando letras e espaços
  Input: dataframe
  Output: dataframe'''
  df1 = dataframe.copy()
  title = lambda x: inflection.titleize(x)
  snakecase = lambda x: inflection.underscore(x)
  spaces = lambda x: x.replace(" ", "")
  cols_old = list(df.columns)
  cols_old = list(map(title, cols_old))
  cols_old = list(map(spaces, cols_old))
  cols_new = list(map(snakecase, cols_old))
  df1.columns = cols_new
  return df1
#========================================================================================-
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America"}
def country_name(country_id):
  ''' Esta função tem por objetivo renomear a coluna de paises com seus respectivos nomes
  Input: dataframe
  Output: dataframe'''
  return COUNTRIES[country_id]
#========================================================================================
def create_price_type(price_range):
  '''Esta função tem por objetivo criar um range de preços, do mais barato ao mais caro
  Input: Dataframe
  Output: Dataframe'''
  if price_range == 1:
    return "cheap"
  elif price_range == 2:
    return "normal"
  elif price_range == 3:
    return "expensive"
  else:
    return "gourmet"
#========================================================================================
COLORS = {
  "3F7E00": "darkgreen",
  "5BA829": "green",
  "9ACD32": "lightgreen",
  "CDD614": "orange",
  "FFBA00": "red",
  "CBCBC8": "darkred",
  "FF7800": "darkred"}
def color_name(color_code):
  ''' Esta função tem por objetivo renomear a coluna de cor com o nome das respectivas cores
  Input: dataframe
  Output: dataframe'''
  return COLORS[color_code]
#========================================================================================
def cluster_map(df1):
    '''Esta função tem por objetivo plotar os marcadores dos restaurantes de forma agrupada no mapa mundi.
    Input: Dataframe
    Output: Mapa'''

    cols = ["restaurant_name", "country_name", "city", "aggregate_rating", "cuisines", "average_cost_for_two","longitude", "latitude", "color"]
    group = ["restaurant_name", "country_name", "city", "cuisines", "color", "aggregate_rating", "average_cost_for_two"]
    df_aux = (df1.loc[:, cols]
            .groupby(group)
            .median()
            .reset_index())
    map = folium.Map()
    marker_cluster = MarkerCluster().add_to(map)

    for index, location_info in df_aux.iterrows():
    # html para deixar a descrição nos marcadores mais organizada
        popup_content = f"""
            <h4>{location_info['restaurant_name']}</h4>
            <p><strong>Culinária:</strong> {location_info['cuisines']}</p>
            <p><strong>Avalição (0-5):</strong> {location_info['aggregate_rating']}</p>
            <p><strong>Preço para dois (R$):</strong> {location_info['average_cost_for_two']}</p>
        """
        folium.Marker([location_info["latitude"],
                    location_info["longitude"]],
                    popup = popup_content,
                    icon = folium.Icon(icon = "cutlery", color = location_info["color"])).add_to(marker_cluster)
    folium_static(map, width = 740, height = 360)
#========================================================================================
def clean_code(df1):
  '''Esta função tem a responsabilidade de limpar o dataframe
  Tipos de limpeza:
  1.Eliminando os dados nulos e duplicados
  2. Renomeando as colunas do dataframe
  3. Preenchimento do nome dos paises
  4. Renomeando a coluna do código do pais
  5. Categorizar os restaurantes por um tipo de culinária
  6. Criação do tipo de categoria de comida
  7. Criação do nome das cores
  8. Renomeando a coluna de cores
  9. Renomear a coluna de entregas
  10.Renomear a coluna de reservas
  Input: Dataframe
  Output: Dataframe'''
  # 1.0 Eliminando os dados nulos e duplicados
  df1.dropna(inplace = True)
  df1.drop_duplicates(keep='first', inplace = True)

  # 2.0 Renomeando as colunas do dataframe
  df1 = rename_columns(df1)

  # 3.0 Preenchimento do nome dos paises
  df1["country_code"] = df1["country_code"].apply(lambda x: country_name(x))

  # 4.0 Renomeando a coluna do código do pais
  df1.rename(columns = {"country_code": "country_name"}, inplace = True)

  # 5.0 Categorizar os restaurantes por um tipo de culinária
  df1["cuisines"] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

  # 6.0 Criação do tipo de categoria de comida
  df1["price_type"] = df1["price_range"].apply(lambda x: create_price_type(x))

  # 7.0 Criação do nome das cores
  df1["rating_color"] = df1["rating_color"].apply(lambda x: color_name(x))

  # 8.0 Renomeando a coluna de cores
  df1.rename(columns = {"rating_color": "color"}, inplace = True)

  # 9.0 Renomear a coluna de entregas
  df1["has_online_delivery"] = df1['has_online_delivery'].apply(lambda x: "não entrega" if x == 0 else "entrega")

  # 10. Renomear a coluna de reservas
  df1["has_table_booking"] = df1['has_table_booking'].apply(lambda x: "não reserva" if x == 0 else "reserva")
  return (df1)

#========================================================================================
# -----------------Inicio da estrutura lógica do código-----------------------------------------------------------
#========================================================================================
# import dataset
#========================================================================================
df = pd.read_csv("./dataset/zomato.csv")
#========================================================================================
# Limpando os dados
#========================================================================================
df1 = clean_code(df)

#========================================================================================
#----------------- Barra lateral ---------------------------------------------------------------------------------
#========================================================================================
# Configurações iniciais
st.markdown("# 🌏Visão geral")
image_path = "./logo.png"
image = Image.open(image_path )
st.sidebar.image(image, width = 120)
st.sidebar.markdown("# Zomato: Food Delivery & Dining")
st.sidebar.markdown("## Never have a bad meal")
st.sidebar.divider()

# Filtro de paises 
st.sidebar.markdown("## Filtro de paises")
country_options = st.sidebar.multiselect(
  "Selecione os paises desejados:",
  df1["country_name"].unique().tolist(),
       default = ["Brazil"])
st.sidebar.divider()

# Aplicando o filtro de paises
linhas_selecionadas = df1["country_name"].isin(country_options)
df1 = df1.loc[linhas_selecionadas, :]

# Crie um botão para acionar o download dos dados tratados
df_download = pd.DataFrame(df1)
csv = df_download.to_csv(index=False)
st.sidebar.markdown("## Dados tratados")
st.divider()
st.sidebar.download_button(label='Download',
                       data=csv,
                       file_name='zomato.csv',
                       mime='text/csv')
st.sidebar.divider()
st.sidebar.markdown("#### Desenvolvido por [Christiano Peres ](https://www.linkedin.com/in/christianods/)")
# =====================================================================
# Layout no streamlit
# =====================================================================
st.markdown("### Dados gerais")
with st.container():
  col1, col2, col3, col4, col5 = st.columns(5, gap = 'small')
  with col1:
    restaurant_unique = df1.loc[:, "restaurant_id"].nunique()
    col1.metric("Restaurantes registrados", restaurant_unique)
  with col2:
    country_unique = df1.loc[:, "country_name"].nunique()
    col2.metric("Paises atendidos", country_unique)
  with col3:
    city_unique = df1.loc[:, "city"].nunique()
    col3.metric("Cidades atendidas", city_unique)
  with col4:
    tot_votes = df1.loc[:, "votes"].sum()
    col4.metric("Total de avaliações", tot_votes)
  with col5:
    cusines_unique = df1.loc[:, "cuisines"].nunique()
    col5.metric("Total de culinárias registradas", cusines_unique)
st.divider()
st.markdown("##### Encontre um parceiro nosso mais próximo 🛵🥡")
cluster_map(df1)
st.divider()
