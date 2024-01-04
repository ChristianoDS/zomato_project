import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = "Home",
    page_icon = "🚀",
    layout = "wide")

#image_path = "./logo.png"
image = Image.open("./logo.png")
st.sidebar.image(image, width = 120)
st.sidebar.markdown("# Zomato: Food Delivery & Dining")
st.sidebar.markdown("## Never have a bad meal")
st.sidebar.divider()
st.sidebar.markdown("#### Desenvolvido por [Christiano Peres ](https://www.linkedin.com/in/christianods/)")
# ======================== Estrutura do home ================================
st.title("Zomato Dashboards")

st.divider()
st.markdown("### Seja muito bem-vindo ao dashboard interativo da Zomato")
'''Esse dashboard tem por objetivo ajudar a empresa de plataforma de restaurantes, Zomato, na tomada de decisão baseada em dados, com isso, foram construídos vários painéis interativos oferecendo insights significantes das visões de paises, cidades, restaurantes e culinárias.'''

st.markdown("### Sobre a Zomato")
'''A Zomato é uma plataforma global de busca de restaurantes e entrega de alimentos, lançada em 2010 e sediada na Índia. Atuando em diversos países ao redor do mundo, a Zomato oferece aos usuários a capacidade de explorar uma vasta gama de restaurantes, seus cardápios, avaliações e classificações. A plataforma facilita a busca por restaurantes, cafés e estabelecimentos de alimentação, além de permitir que os usuários façam pedidos de comida online para entrega em casa. 
 Com uma missão centrada na conectividade alimentar, a Zomato valoriza a diversidade culinária e busca oferecer uma experiência gastronômica única para seus usuários. Seus valores incluem a transparência, a inovação e a paixão pela comida, buscando constantemente melhorar a maneira como as pessoas descobrem, compartilham e desfrutam de refeições. A empresa desempenha um papel significativo na transformação digital do setor de alimentos e bebidas, proporcionando uma plataforma conveniente e abrangente para a comunidade gastronômica global.'''

st.markdown("### Aquisição dos dados")
'''Embora a Zomato seja uma empresa real, os dados foram obtidos por meio de plataformas públicas de dados, como o Kaggle (https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv).'''
'''Não apresentando relação direta com a empresa.'''

st.markdown("### Como utilizar esse dashboard")
'''Esse dashboard foi dividido em 3 abas:
 - 🌏 Visão geral '''
'''Aqui são apresentadas métricas gerais da Zomato, além de um mapa mundi para vizualização dos seus restaurantes parceiros.'''

'''- 📊 Dashboard '''
'''Nessa aba estão representados painéis interativos referentes as visões de paises, cidades, restaurantes e culinária.'''

'''✉️ Contato '''
'''Aba de contato traz as principais formas que você pode entrar em contato comigo.'''
st.divider()
