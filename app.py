import streamlit as st 
st.title ("Motorsney- Aluguel de carros")
st.subheader("O lugar aonde as lendas compram")
st.sidebar.title("Escolha um modelo")
st.sidebar.image('logo.png')


carros = ['BMW','Mustang','Porsche','Fusca','Toro']
opcao = st.sidebar.selectbox("Escolha o carro que deseja alugar",carros)


st.image(f"{opcao}.png", width=1000)

st.markdown(f"## Você alugou o modelo: {opcao}")
st.markdown("---")