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
st.set_page_config(page_title='Dashboards', page_icon='📊', layout='wide')
#========================================================================================
#                              Funções
#========================================================================================
# ---------------------------- Aba Paises -----------------------------------------------
def rest_country(df1):  
  df_aux = (df1.loc[:, ["restaurant_id","country_name"]]
                  .groupby("country_name")
                  .nunique()
                  .sort_values("restaurant_id", ascending = False)
                  .head(5)
                  .reset_index())
  # Gráfico
  fig = px.bar(df_aux, x = "country_name",
        y = "restaurant_id",
        text = "restaurant_id",
        labels = {"country_name":"Paises", "restaurant_id":"Restaurantes atendidos"},
        title = "Top 10 Paises com mais restaurantes registrados",
        color = "restaurant_id",
        color_continuous_scale=px.colors.sequential.Reds)
  return fig
#========================================================================================
# ---------------------------- Aba Paises -----------------------------------------------
def country_city(df1):
  df_aux = (df1.loc[:, ["country_name","city"]]
                .groupby("country_name")
                .nunique()
                .sort_values("city", ascending = False)
                .head(5)
                .reset_index())
  df_aux.columns = ["country_name", "number_of_city"]
  # Gráfico
  fig = px.bar(df_aux,
                  x = "country_name",
                  y = "number_of_city",
                  title = "Top 10 Paises com mais cidades atendidas",
                  labels = {"country_name":"Paises", "number_of_city": "Cidades atendidas"},
                  text = "number_of_city",
                  color="number_of_city",  # Adicionando a variável de cor
                  color_continuous_scale=px.colors.sequential.Reds)
  return fig
#========================================================================================
# ---------------------------- Aba Paises -----------------------------------------------
def country_cuisines (df1):
  df_aux = (df1.loc[:, ["country_name","cuisines"]]
          .groupby("country_name")
          .nunique()
          .sort_values("cuisines", ascending = False)
          .head(5)
          .reset_index())
  # Gráfico
  fig = px.bar(df_aux, x = "country_name",
       y = "cuisines",
       text = "cuisines",
       labels = {"country_name":"Paises", "cuisines":"Tipos de culinárias diferentes"},
       title = "Top 5 paises com culinárias diversificadas",
       color = "cuisines",
       color_continuous_scale= px.colors.sequential.Reds)
  return fig
#========================================================================================
# ---------------------------- Aba Paises -----------------------------------------------
def country_votes (df1):
  df_aux = (df1.loc[:, ["country_name", "votes"]]
          .groupby("country_name")
          .sum()
          .sort_values("votes", ascending = False)
          .head(5)
          .reset_index())
  # Gráficos
  fig = px.bar(df_aux, x = "country_name",
       y = "votes",
       title = "Top 5 paises com mais avaliações feitas",
       labels = {"country_name":"Paises", "votes":"Avaliações"},
       text = "votes",
       color = "votes",
       color_continuous_scale=px.colors.sequential.Reds)
  return fig
#========================================================================================
# ---------------------------- Aba Paises -----------------------------------------------
def country_rate (df1):
  df_aux = (df1.loc[:, ["country_name", "aggregate_rating"]]
          .groupby("country_name")
          .mean()
          .sort_values("aggregate_rating", ascending = False)
          .round(2)
          .head(5)
          .reset_index())
  # Gráfico
  fig = px.bar(df_aux, x = "country_name",
       y = "aggregate_rating",
       title = "Média de avaliações por paises",
       labels = {"country_name":"Paises", "aggregate_rating":"Média de avaliações"},
       text = "aggregate_rating",
       color = "aggregate_rating",
       color_continuous_scale=px.colors.sequential.Reds)
  return fig
#========================================================================================
# ---------------------------- Aba Paises -----------------------------------------------
def country_gourmet (df1):
  linhas = df1["price_type"] == "gourmet"
  df_aux = (df1.loc[linhas, ["restaurant_id","country_name"]]
          .groupby("country_name")
          .count()
          .sort_values("restaurant_id", ascending = False)
          .head(5)
          .reset_index())
# Gráfico
  fig = px.bar(df_aux, x = "country_name",
       y = "restaurant_id",
       labels = {"country_name":"Paises", "restaurant_id":"Restaurantes com preço gourmet"},
       text = "restaurant_id",
       title = "Top 5 paises que possuem mais restaurantes com preço gourmet",
       color = "restaurant_id",
       color_continuous_scale= px.colors.sequential.Reds)
  return fig
#========================================================================================
# ---------------------------- Aba Cidade -----------------------------------------------
def city_rest (df1):
  df_aux = (df1.loc[:, ["city","restaurant_id"]]
            .groupby("city")
            .nunique()
            .sort_values("restaurant_id", ascending =  False)
            .head(10)
            .reset_index())
  df_aux.columns = ["Cidades", "Restaurantes atendidos"]
  return df_aux
#========================================================================================
# ---------------------------- Aba Cidade -----------------------------------------------
def city_rest_4 (df1):
  linhas = df1["aggregate_rating"] > 4
  df_aux = (df1.loc[linhas, ["city","restaurant_id"]]
            .groupby("city")
            .nunique()
            .sort_values("restaurant_id", ascending =  False)
            .head(5)
            .reset_index())
  # Gráficos
  fig = px.bar(df_aux, x = "city",
        y = "restaurant_id",
        title = "Top 5 cidades com restaurantes com média de avaliação maior que 4",
        labels = {"city":"Cidades", "restaurant_id":"Restaurantes"},
        text = "restaurant_id",
        color = "restaurant_id",
        color_continuous_scale=px.colors.sequential.Reds)
  return fig
#========================================================================================
# ---------------------------- Aba Cidade -----------------------------------------------
def city_rest_menor (df1):
  linhas = df1["aggregate_rating"] < 2.5
  df_aux = (df1.loc[linhas, ["city","restaurant_id"]]
            .groupby("city")
            .nunique()
            .sort_values("restaurant_id", ascending =  False)
            .head(5)
            .reset_index())
  # Gráficos
  fig = px.bar(df_aux, x = "city",
        y = "restaurant_id",
        title = "Top 5 cidades com restaurantes com média abaixo de 2.5",
        labels = {"city":"Cidades", "restaurant_id":"Restaurantes"},
        text = "restaurant_id",
        color = "restaurant_id",
        color_continuous_scale=px.colors.sequential.Reds)
  return fig
#========================================================================================
# ---------------------------- Aba Cidade -----------------------------------------------
def city_prato_mais_caro (df1):
  df_aux = (df1.loc[:, ["city","average_cost_for_two"]]
          .groupby("city")
          .mean()
          .sort_values("average_cost_for_two", ascending =  False)
          .round(2)
          .head(5)
          .reset_index())
  # Gráficos
  fig = px.bar(df_aux, x = "city",
        y = "average_cost_for_two",
        title = "Top 5 Cidades com maiores valores de pratos para duas pessoas",
        labels = {"city":"Cidades", "average_cost_for_two":"Média do prato para duas pessoas"},
        text = "average_cost_for_two",
        color = "average_cost_for_two",
        color_continuous_scale=px.colors.sequential.Reds)
  return fig
#========================================================================================
# ---------------------------- Aba Cidade -----------------------------------------------
def city_cuisines (df1):
  df_aux = (df1.loc[:, ["city","cuisines"]]
            .groupby("city")
            .nunique()
            .sort_values("cuisines", ascending =  False)
            .head(5)
            .reset_index())
  # Gráficos
  fig = px.bar(df_aux, x = "city",
        y = "cuisines",
        title = "Top 5 cidades com mais culinárias distintas",
        labels = {"city":"Cidades", "cuisines":"Culinárias distintas"},
        text = "cuisines",
        color = "cuisines",
        color_continuous_scale=px.colors.sequential.Reds)
  return (fig)
#========================================================================================
# ---------------------------- Aba Restaurante ------------------------------------------
def rest_rate (df1):
  df_aux = (df1.loc[:, ["restaurant_id", "restaurant_name","aggregate_rating", "country_name"]]
          .groupby(["country_name", "restaurant_name"])
          .mean()
          .sort_values(["aggregate_rating", "restaurant_id"], ascending =  [False, True])
          .head(10)
          .reset_index())
  df_final = df_aux[["restaurant_name", "country_name","aggregate_rating"]]
  df_final.columns = ["Restaurante", "Pais","Média de avaliações (5/5)"]
  return df_final
#========================================================================================
# ---------------------------- Aba Restaurante ------------------------------------------
def rest_expensive (df1):
  linhas = (df1["price_type"] == "gourmet") | (df1["price_type"] == "expensive")
  df_aux = (df1.loc[linhas, ["restaurant_name","restaurant_id", "country_name", "aggregate_rating"]
                    ].groupby(["restaurant_name", "restaurant_id","country_name"])
                    .mean()
                    .sort_values (["aggregate_rating","restaurant_id"], ascending = [False,True])
                    .reset_index()
                    .head(10))
  df_aux.drop_duplicates(subset = "restaurant_name", keep = "first")
  df_aux2 = df_aux[["restaurant_name", "country_name", "aggregate_rating"]]
  df_aux2.columns = ["Restaurante","Pais","Avaliações médias (5/5)"]
  return df_aux2
#========================================================================================
# ---------------------------- Aba Restaurante ------------------------------------------
def rest_cheap(df1):
  linhas = df1["price_type"] == "cheap"
  df_aux = (df1.loc[linhas, ["restaurant_name","restaurant_id", "country_name", "aggregate_rating"]
                    ].groupby(["restaurant_name", "restaurant_id","country_name"])
                    .mean()
                    .sort_values (["aggregate_rating","restaurant_id"], ascending = [False,True])
                    .reset_index()
                    .head(10))
  df_aux.drop_duplicates(subset = "restaurant_name", keep = "first")
  df_aux2 = df_aux[["restaurant_name", "country_name", "aggregate_rating"]]
  df_aux2.columns = ["Restaurante","Pais","Avaliações médias (5/5)"]
  return df_aux2
#========================================================================================
# ---------------------------- Aba Restaurante ------------------------------------------
def rest_online_delivery (df1):
  df_aux = (df1.loc[:, ["has_online_delivery", "votes"]]
          .groupby("has_online_delivery")
          .mean()
          .sort_values("votes", ascending = False)
          .reset_index())
  # Gráfico
  fig = px.pie(df_aux, names = "has_online_delivery",
        values = "votes",
        color = "has_online_delivery",
        color_discrete_map={"Fazem entrega online": "darkred", "Não fazem entrega online": "lightcoral"},
        title = "Restaurantes com mais avaliações recebidas")
  return fig
#========================================================================================
# ---------------------------- Aba Restaurante ------------------------------------------
def rest_table_booking (df1):
  df_aux = (df1.loc[:, ["has_table_booking", "average_cost_for_two"]]
          .groupby("has_table_booking")
          .mean()
          .sort_values("average_cost_for_two", ascending = False)
          .reset_index())
  # Gráfico
  fig = px.pie(df_aux, names = "has_table_booking",
        values = "average_cost_for_two",
        color = "has_table_booking",
        title = ("Restaurantes com maior valor médio de um prato para duas pessoas"),
        color_discrete_map={"Aceitam reserva": "darkred", "Não aceitam reserva": "lightcoral"})
  return fig
#========================================================================================
# ---------------------------- Aba Culinária --------------------------------------------
def cuisines_votes (df1):
  df_aux = (df1.loc[:, ["cuisines","aggregate_rating", "votes"]]
          .groupby("cuisines")
          .agg({'aggregate_rating': "mean", 'votes': 'sum'})
          .sort_values(["aggregate_rating", "votes"], ascending = [False,False])
          .round(2)
          .head(10)
          .reset_index())
  df_aux2 = df_aux.loc[:, ["cuisines","votes" ,"aggregate_rating"]]
  df_aux2.columns =  ["Culinária", "Avaliações", "Nota média"]
  return df_aux2
#========================================================================================
# ---------------------------- Aba Culinária --------------------------------------------
def cuisines_best_rest (df1, cuisines):
  '''cuisines é o tipo de culinária desejado
  Italian
  Japanese
  Brazilian
  Ramen
  Egyptian
  Ottoman'''
  linhas = df1["cuisines"] == cuisines
  df_aux = (df1.loc[linhas, ["restaurant_id", "aggregate_rating", "restaurant_name", "votes"]]
            .groupby("restaurant_name")
            .mean()
            .sort_values(["aggregate_rating", "restaurant_id"], ascending = [False, True])
            .head(1)
            .reset_index())
  df_aux2 = df_aux.loc[:, ["restaurant_name","votes" ,"aggregate_rating"]]
  df_aux2.columns =  ["Restaurante", "Avaliações", "Nota média"]
  return df_aux2
#========================================================================================
# ---------------------------- Aba Culinária --------------------------------------------
def rest_delivery (df1):
  linhas = (df1["has_online_delivery"] == "Fazem entrega online") & (df1["is_delivering_now"] == 1)
  df_aux = df1.loc[linhas, "cuisines"].value_counts().head(10).reset_index()
  df_aux = pd.DataFrame(df_aux)
  df_aux.columns = ["Culinária","Restaurantes que aceitam pedidos online e fazem entregas"]
  return df_aux
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
# ---------------------------- Limpeza do código ----------------------------------------
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
  df1["has_online_delivery"] = df1['has_online_delivery'].apply(lambda x: "Não fazem entrega online" if x == 0 else "Fazem entrega online")

  # 10. Renomear a coluna de reservas
  df1["has_table_booking"] = df1['has_table_booking'].apply(lambda x: "Não aceitam reserva" if x == 0 else "Aceitam reserva")
  return (df1)

#========================================================================================
# -----------------Inicio da estrutura lógica do código----------------------------------
#========================================================================================
# import dataset
#========================================================================================
df = pd.read_csv("./dataset/zomato.csv")
#========================================================================================
# Limpando os dados
#========================================================================================
df1 = clean_code(df)
#========================================================================================
#----------------- Barra lateral --------------------------------------------------------
#========================================================================================
# Configurações iniciais
st.markdown("# 📊 Dashboards")
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
st.divider()
st.sidebar.markdown("## Dados tratados")
st.sidebar.download_button(label='Download',
                       data=csv,
                       file_name='zomato.csv',
                       mime='text/csv')
st.sidebar.divider()
st.sidebar.markdown("#### Desenvolvido por [Christiano Peres ](https://www.linkedin.com/in/christianods/)")

# =====================================================================
# Layout no streamlit
# =====================================================================
#Criando os containers para o dashboard 
tab1, tab2, tab3, tab4 = st.tabs (["🗺️ Paises", "🏙️ Cidades", "🍽️ Restaurantes", "🍜 Culinárias"]) 
# cada tab é um menu para as visões de negócios

# ----------------------- Visão Paises ----------------------------------
with tab1:
  st.markdown ("### Métricas dos paises 🗺️")
  st.divider()
  with st.container():
    col1, col2 = st.columns(2)
    with col1:
      fig = rest_country(df1)
      st.plotly_chart(fig, use_container_width=True)
  with col2:
    fig = country_city(df1)
    st.plotly_chart(fig, use_container_width=True)
  st.divider()

  with st.container():
    col1, col2 = st.columns(2)
  with col1:
    fig = country_cuisines(df1)
    st.plotly_chart(fig, use_container_width=True)
  with col2:
    fig = country_votes(df1)
    st.plotly_chart(fig, use_container_width=True)
  st.divider()

  with st.container():
    col1, col2 = st.columns(2)
  with col1:
    fig = country_rate(df1)
    st.plotly_chart(fig, use_container_width=True)
  with col2:
    fig = country_gourmet(df1)
    st.plotly_chart(fig, use_container_width=True)
  st.divider()
# ----------------------- Visão Cidades ----------------------------------
with tab2:
  st.markdown ("### Métricas das cidades 🏙️")
  st.divider()
  with st.container():
    data_frame = city_rest(df1)
    st.markdown("#### Top 10 cidades que atendem mais restauranetes")
    st.dataframe(data_frame, hide_index=True)
  st.divider()

  with st.container():
    col1, col2 = st.columns(2)
  with col1:
    fig = city_rest_4(df1)
    st.plotly_chart(fig, use_container_width=True)
  with col2:
    fig = city_rest_menor(df1)
    st.plotly_chart(fig, use_container_width=True)
  st.divider()

  with st.container():
    col1, col2 = st.columns(2)
  with col1:
    fig = city_prato_mais_caro(df1)
    st.plotly_chart(fig, use_container_width=True)
  with col2:
    fig = city_cuisines(df1)
    st.plotly_chart(fig, use_container_width=True)
  st.divider()

# ----------------------- Visão Restaurantes ----------------------------------
with tab3:
  st.markdown ("### Métricas dos restaurantes 🍽️")
  st.divider()
  with st.container():
    data_frame = rest_rate(df1)
    st.markdown("#### Top 10 restaurantes mais bem avaliados")
    st.dataframe(data_frame, hide_index=True)

  with st.container():
    col1, col2 = st.columns(2)
  with col1:
    st.markdown("#### Top 10 restaurantes mais bem avaliados com comida considerada cara")
    data_frame = rest_expensive(df1)
    st.dataframe(data_frame, hide_index=True)
  with col2:
    st.markdown("#### Top 10 restaurantes mais bem avaliados com comida considerada barata")
    data_frame = rest_cheap(df1)
    st.dataframe(data_frame, hide_index=True)
  st.divider()

  with st.container():
    col1, col2 = st.columns(2)
  with col1:
    fig = rest_online_delivery(df1)
    st.plotly_chart(fig, use_container_width=True)
  with col2:
    fig = rest_table_booking(df1)
    st.plotly_chart(fig, use_container_width=True)
  st.divider()

  # ----------------------- Visão Culinária----------------------------------
with tab4:
  st.markdown ("### Métricas das culinária 🍜")
  st.divider()
  with st.container():
    st.markdown("#### Top 10 culinárias mais bem avaliadas")
    dataframe = cuisines_votes(df1)
    st.dataframe(dataframe, hide_index=True)
  st.divider()
    
  with st.container():
    st.markdown("### Melhores restaurantes cadastrados por culinárias: ")
    col1, col2, col3 = st.columns(3)
  with col1:
    best_italian = cuisines_best_rest(df1, "Italian")
    best_rest_italian = best_italian["Nota média"]
    best_name_italian = best_italian["Restaurante"].to_string(index = False)
    if best_rest_italian.empty:
      st.markdown(f"##### Culinária Italiana:  Sem registro")
      col1.metric("Nota (5/5): ", "-")
    else:
      st.markdown(f"##### Culinária Italiana:  {best_name_italian}")
      col1.metric("Nota (5/5): ", best_rest_italian)

  with col2:
    best_japa = cuisines_best_rest(df1, "Japanese")
    best_rest_japa = best_japa["Nota média"]
    best_name_japa = best_japa["Restaurante"].to_string(index = False)
    if best_rest_japa.empty:
      st.markdown(f"##### Culinária Japonesa:  Sem registro")
      col2.metric("Nota (5/5): ", "-")
    else:
      st.markdown(f"##### Culinária Egípcia:  {best_name_japa}")
      col2.metric("Nota (5/5): ", best_rest_japa)

  with col3:
    best_br = cuisines_best_rest(df1, "Brazilian")
    best_rest_br = best_br["Nota média"]
    best_name_br = best_br["Restaurante"].to_string(index = False)
    if best_rest_br.empty:
      st.markdown(f"##### Culinária Brasileira:  Sem registro")
      col3.metric("Nota (5/5): ", "-")
    else:
      st.markdown(f"##### Culinária Brasileira:  {best_name_br}")
      col3.metric("Nota (5/5): ", best_rest_br)

  with st.container():
    col1, col2, col3 = st.columns(3)
  with col1:
    best_ramen = cuisines_best_rest(df1, "Ramen")
    best_rest_ramen = best_ramen["Nota média"]
    best_name_ramen = best_ramen["Restaurante"].to_string(index = False)
    if best_rest_ramen.empty:
      st.markdown(f"##### Culinária Ramen:  Sem registro")
      col1.metric("Nota (5/5): ", "-")
    else:
      st.markdown(f"##### Culinária Ramen:  {best_name_ramen}")
      col1.metric("Nota (5/5): ", best_rest_ramen)

  with col2:
    best_egy = cuisines_best_rest(df1, "Egyptian")
    best_rest_egy = best_egy["Nota média"]
    best_name_egy = best_egy["Restaurante"].to_string(index = False)
    if best_rest_egy.empty:
      st.markdown(f"##### Culinária Egípcia:  Sem registro")
      col2.metric("Nota (5/5): ", "-")
    else:
      st.markdown(f"##### Culinária Egípcia:  {best_name_egy}")
      col2.metric("Nota (5/5): ", best_rest_egy)

  with col3:
    best_fish = cuisines_best_rest(df1, "Fresh Fish")
    best_rest_fish = best_fish["Nota média"]
    best_name_fish = best_fish["Restaurante"].to_string(index = False)
    if best_rest_fish.empty:
      st.markdown(f"##### Culinária Peixe fresco:  Sem registro")
      col3.metric("Nota (5/5): ", "-")
    else:
      st.markdown(f"##### Culinária Peixe fresco:  {best_name_fish}")
      col3.metric("Nota (5/5): ", best_rest_fish)
  st.divider()
  
  with st.container():
    st.markdown("#### Culinárias que possuem mais restaurantes que aceitam pedidos online e fazem entregas")
    data_frame = rest_delivery(df1)
    if data_frame.empty:
      st.markdown("Sem registros")
    else:
      st.dataframe(data_frame, hide_index=True)
  st.divider()
