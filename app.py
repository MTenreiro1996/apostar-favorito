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

# LISTA CORRIGIDA: Adicionadas as opções 1 e 2 para a escolha da percentagem
stake_opt = st.sidebar.radio("Percentagem de Risco (Flat Stake)", [1, 2], format_func=lambda x: f"{x}%")
stake_dinheiro = banca_atual * (stake_opt / 100)
st.sidebar.info(f"**Tua Stake Fixa:** {stake_dinheiro:.2f}€")

# ABAS DA APLICAÇÃO
tab1, tab2 = st.tabs(["📋 Lista de Alvos Semanais", "📊 Calculadora Live (Minuto 55-60)"])

with tab1:
    st.subheader("📌 Condições Obrigatórias de Seleção (Pré-Live)")
    st.markdown("""
    Antes de registares qualquer jogo para a semana, garante que ele cumpre estes **3 critérios estritos**:
    1. 🏟️ **Fator Casa:** A equipa favorita joga obrigatoriamente no seu próprio estádio.
    2. 📈 **Odds de Abertura:** A odd inicial para a vitória do visitado (1) está estritamente entre **1.20 e 1.35**.
    3. 🏆 **Teste da Classificação:** O favorito está no **Top 4** da tabela e o adversário está na metade inferior.
    """)
    st.markdown("---")
    
    st.subheader("🔍 A Minha Agenda de Trading da Semana")
    st.markdown("Planeia a tua semana na segunda-feira. Deixa os alvos anotados por blocos de dias:")
    
    jogos_meio_semana = st.text_area("Jogos de Terça a Quinta-Feira:", placeholder="Ex:\nTerça 20h00: Sporting vs Farense\nQuarta 19h45: Barcelona vs Getafe")
    jogos_fim_semana = st.text_area("Jogos de Sexta a Domingo:", placeholder="Ex:\nSábado 15h30: Real Madrid vs Alavés\nDomingo 18h00: Benfica vs Gil Vicente")

with tab2:
    st.subheader("⚡ Validação de Massacre Real (SofaScore / FlashScore)")
    st.markdown("Chegou o **minuto 55-60** e o jogo continua **0-0**? Confirma as estatísticas e marca com um **certo (✓)**:")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Estatísticas de Volume:")
        criterio_remates = st.checkbox("O favorito tem pelo menos 2 ou 3 Remates no Alvo / À Baliza? (Ver aba 'Estatísticas' do SofaScore ou FlashScore)")
        criterio_chances = st.checkbox("O favorito já criou 1 ou 2 Grandes Chances de Golo? (Ver aba 'Estatísticas' do SofaScore)")
        criterio_ataques = st.checkbox("O favorito tem um volume alto de Ataques Perigosos? (Ver aba 'Estatísticas' do FlashScore)")
        
    with col2:
        st.markdown("#### 👁️ Leitura Visual e Contexto:")
        grafico_sufoco = st.checkbox("O gráfico mostra barras altas do favorito coladas ao topo nos últimos 10 minutos? (Ver 'Attack Momentum' no SofaScore ou barras cinzentas na FlashScore)")
        bloco_baixo = st.checkbox("O adversário está totalmente trancado na sua área a sofrer sufoco?")
        sub_ofensivas = st.checkbox("O treinador do favorito já fez ou está a fazer substituições ofensivas para ganhar? (Ver aba 'Alinhamentos')")

    st.markdown("### 📢 Veredito da Ferramenta:")
    
    # O sinal verde só dispara se todos os critérios forem validados com "certo" pelo utilizador
    criterios_validos = (
        criterio_remates and 
        criterio_chances and 
        criterio_ataques and 
        grafico_sufoco and 
        bloco_baixo and 
        sub_ofensivas
    )

    if criterios_validos:
        st.error(f"🚨 **ENTRADA APROVADA (BACK FAVORITO)** 🚨\n\n"
                 f"• **Aposta a colocar:** {stake_dinheiro:.2f}€ na OrbitX\n"
                 f"• **Plano de Saída:** Fazer Cash Out imediato assim que surgir o 1-0.\n"
                 f"• **Stop Loss:** Se continuar 0-0 ao minuto 78-80, fazer Cash Out na OrbitX e aceitar o red parcial.")
    else:
        st.warning("⚠️ **AGUARDAR / NÃO ENTRAR** ⚠️\n\n"
                   "Garante que todos os critérios de massacre acima estão marcados com um certo. Se faltar apenas um, não arrisques o teu dinheiro.")
