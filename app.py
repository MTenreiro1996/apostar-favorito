import streamlit as st
import urllib.request
import json
from datetime import datetime

# Configuração da página do Streamlit
st.set_page_config(page_title="Radar Position Trading", page_icon="⚽", layout="wide")

st.title("⚽ Radar Position Trading - Futebol Live")
st.markdown("---")

# BANCA E GESTÃO DE RISCO (Guardado na sessão da app)
if 'banca' not in st.session_state:
    st.session_state.banca = 100.0

st.sidebar.header("💰 Gestão de Banca (OrbitX)")
banca_atual = st.sidebar.number_input("Valor da Banca Atual (€)", min_value=1.0, value=st.session_state.banca, step=10.0)
st.session_state.banca = banca_atual

# Definição estrita de risco: 1% ou 2% sem Martingale
stake_opt = st.sidebar.radio("Percentagem de Risco (Flat Stake)", [1, 2], format_func=lambda x: f"{x}%")
stake_dinheiro = banca_atual * (stake_opt / 100)
st.sidebar.info(f"**Tua Stake Fixa:** {stake_dinheiro:.2f}€")

# FEEDS DE DADOS SEGUROS E GRATUITOS (Época 2026)
LEAGUE_URLS = {
    "Premier League (Inglaterra)": "https://fixturedownload.com",
    "La Liga (Espanha)": "https://fixturedownload.com",
    "Liga Portugal": "https://fixturedownload.com"
}

# ABA DE TRIAGEM DA MANHÃ E CALCULADORA LIVE
tab1, tab2 = st.tabs(["📋 Radar Pré-Live (Jogos do Dia)", "📊 Calculadora Live (Minuto 55-60)"])

with tab1:
    hoje = datetime.now().strftime("%Y-%m-%d")
    st.subheader(f"🔍 Jogos Agendados para Hoje: {hoje}")
    
    encontrou = False
    
    for nome_liga, url in LEAGUE_URLS.items():
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                dados = json.loads(response.read().decode())
                
                jogos_liga = [j for j in dados if j.get("Date", "").startswith(hoje)]
                
                if jogos_liga:
                    st.write(f"### {nome_liga}")
                    for jogo in jogos_liga:
                        casa = jogo.get("HomeTeam")
                        fora = jogo.get("AwayTeam")
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.info(f"🏟️ **{casa}** vs {fora}")
                        with col2:
                            st.markdown(f"**Ação:** Validar se a Odd Inicial do **{casa}** está entre 1.20 e 1.30 na OrbitX.")
                    encontrou = True
        except Exception:
            st.warning(f"⚠️ Servidor da liga {nome_liga} temporariamente indisponível.")
            
    if not encontrou:
        st.success("Sem jogos de elite listados para as próximas horas desta data.")

with tab2:
    st.subheader("⚡ Análise de Massacre em Tempo Real")
    st.markdown("Lança os dados do **SofaScore** ou **Flashscore** a partir do minuto 55 com o jogo **0-0**.")

    c1, c2, c3 = st.columns(3)
    with c1:
        odd_live = st.number_input("Odd Atual do Favorito (Back)", min_value=1.0, value=1.85, step=0.05)
    with c2:
        ataques_perigosos = st.number_input("Ataques Perigosos do Favorito (Últimos 10 min)", min_value=0, value=25)
    with c3:
        pressao_grafico = st.number_input("Gráfico de Pressão SofaScore (0 a 100)", min_value=0, max_value=100, value=75)

    st.markdown("#### Filtros de Contexto Real:")
    sub_ofensivas = st.checkbox("O treinador mexeu para meter a equipa mais ofensiva?")
    bloco_baixo = st.checkbox("O adversário está trancado na área a sofrer remates/cantos?")

    st.markdown("### 📢 Veredito da Ferramenta:")
    
    criterios_validos = (
        odd_live >= 1.50 and 
        ataques_perigosos >= 15 and 
        pressao_grafico >= 60 and 
        sub_ofensivas and 
        bloco_baixo
    )

    if criterios_validos:
        st.error(f"🚨 **ENTRADA APROVADA (BACK FAVORITO)** 🚨\n\n"
                 f"• **Aposta a colocar:** {stake_dinheiro:.2f}€ na OrbitX\n"
                 f"• **Plano de Saída:** Fazer Cash Out imediato assim que surgir o 1-0.\n"
                 f"• **Stop Loss:** Se continuar 0-0 ao minuto 78-80, fazer Cash Out e aceitar o red parcial.")
    else:
        st.warning("⚠️ **AGUARDAR / NÃO ENTRAR** ⚠️\n\n"
                   "Os critérios de massacre ou valor de odd ainda não foram totalmente atingidos. Não arrisques a tua banca.")
