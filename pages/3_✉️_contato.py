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
st.set_page_config(page_title='Contato',page_icon='✉️',layout='wide')
#========================================================================================
#                           Funções
#========================================================================================


#========================================================================================
#----------------- Barra lateral ---------------------------------------------------------------------------------
#========================================================================================
# Configurações iniciais
st.markdown("# 📱✉️ Entre em contato")
image_path = "./logo.png"
image = Image.open(image_path )
st.sidebar.image(image, width = 120)
st.sidebar.markdown("# Zomato: Food Delivery & Dining")
st.sidebar.markdown("## Never have a bad meal")
st.sidebar.divider()
st.sidebar.markdown("##### Powered by Christiano Peres - Comunidade DS")

# =====================================================================
# Layout no streamlit
# =====================================================================
st.header("Ficou com dúvida ❓❓")
st.divider()
st.markdown("#### Portifólio de projetos 🚀: https://christianods.github.io/portifolio_projetos")
st.markdown("#### Linkedin 🔗: https://www.linkedin.com/in/christianods")
st.markdown("#### Github 💻: https://github.com/ChristianoDS")
st.markdown("#### Email ✉️: christianoperes21@gmail.com")
st.markdown("#### Discord 💬: christianoperes")
st.divider()
          