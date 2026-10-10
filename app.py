import streamlit as st

st.set_page_config(page_title="Radar Position Trading", page_icon="⚽", layout="wide")

st.title("⚽ Radar Position Trading - Futebol Live")
st.markdown("---")

# BANCA E GESTÃO DE RISCO
if 'banca' not in st.session_state:
    st.session_state.banca = 100.0

st.sidebar.header("💰 Gestão de Banca (OrbitX)")
banca_atual = st.sidebar.number_input("Valor da Banca Atual (€)", min_value=1.0, value=st.session_state.banca, step=10.0)
st.session_state.banca = banca_atual

stake_opt = st.sidebar.radio("Percentagem de Risco (Flat Stake)", [1, 2], format_func=lambda x: f"{x}%")
stake_dinheiro = banca_atual * (stake_opt / 100)
st.sidebar.info(f"**Tua Stake Fixa:** {stake_dinheiro:.2f}€")

tab1, tab2 = st.tabs(["📋 Radar Pré-Live (Os Teus Alvos)", "📊 Calculadora Live (Minuto 55-60)"])

with tab1:
    st.subheader("🔍 A Minha Lista de Vigilância para Hoje")
    st.markdown("De manhã, encontra os favoritos em casa (Odd 1.20 - 1.30) e regista-os aqui:")
    
    jogo_introduzido = st.text_input("Escreve o jogo do dia:", placeholder="Ex: Sporting vs Casa Pia")
    
    if jogo_introduzido:
        st.info(f"🎯 **Alvo Ativo:** {jogo_introduzido}")
        st.markdown("**Plano:** Se chegar ao **minuto 55-60 com 0-0**, abre a tua aplicação desportiva e vai para a aba ao lado.")
    else:
        st.write("Introduz um jogo acima para ativar o radar.")

with tab2:
    st.subheader("⚡ Validação de Massacre Real")
    st.markdown("Insere os números reais que estás a ver na tua aplicação a partir do minuto 55 com o jogo **0-0**.")

    col1, col2 = st.columns(2)
    
    with col1:
        odd_live = st.number_input("Odd Atual do Favorito na Bolsa (Ver na OrbitX)", min_value=1.0, value=1.80, step=0.05)
        remates_no_alvo = st.number_input("Remates NO ALVO / À Baliza do Favorito (Ver na aba 'Estatísticas' do SofaScore ou FlashScore)", min_value=0, value=3)
        atq_perigosos_fav = st.number_input("Ataques Perigosos do FAVORITO (Ver na aba 'Estatísticas' do FlashScore)", min_value=0, value=50)
        atq_perigosos_adv = st.number_input("Ataques Perigosos do ADVERSÁRIO (Ver na aba 'Estatísticas' do FlashScore)", min_value=0, value=20)
        
    with col2:
        st.markdown("#### Leitura Visual do Gráfico em Direto:")
        grafico_sufoco = st.checkbox("O gráfico mostra barras altas do favorito coladas ao topo nos últimos 10 minutos? (Ver gráfico 'Attack Momentum' no SofaScore ou barras cinzentas na FlashScore)")
        adversario_morto = st.checkbox("O adversário quase não atacou nos últimos 10 minutos? (Ver a ausência de barras contrárias no SofaScore ou FlashScore)")
        sub_ofensivas = st.checkbox("O treinador do favorito fez substituições para meter a equipa mais ofensiva? (Ver aba 'Alinhamentos' / Notícias do jogo)")

    st.markdown("### 📢 Veredito da Ferramenta:")
    
    # Critérios recalculados: Sem cantos, focando em Remates, Ataques Perigosos e Leitura Visual
    criterios_validos = (
        odd_live >= 1.50 and 
        remates_no_alvo >= 2 and 
        atq_perigosos_fav >= (atq_perigosos_adv * 2) and 
        grafico_sufoco and 
        adversario_morto and 
        sub_ofensivas
    )

    if criterios_validos:
        st.error(f"🚨 **ENTRADA APROVADA (BACK FAVORITO)** 🚨\n\n"
                 f"• **Aposta a colocar:** {stake_dinheiro:.2f}€ na OrbitX\n"
                 f"• **Plano de Saída:** Fazer Cash Out imediato assim que surgir o 1-0.\n"
                 f"• **Stop Loss:** Se continuar 0-0 ao minuto 78-80, fazer Cash Out na OrbitX e aceitar o red parcial.")
    else:
        st.warning("⚠️ **AGUARDAR / NÃO ENTRAR** ⚠️\n\n"
                   "Os critérios combinados de massacre e valor de odd ainda não foram totalmente atingidos. Não arrisques o teu dinheiro.")
