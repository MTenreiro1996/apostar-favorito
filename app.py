import streamlit as st

# Configuração da página do Streamlit (Layout largo e limpo)
st.set_page_config(page_title="Radar Position Trading", page_icon="⚽", layout="wide")

st.title("⚽ Radar Position Trading - Futebol Live")
st.markdown("---")

# 1. QUADRO DE CONDIÇÕES OBRIGATÓRIAS (PRÉ-LIVE)
st.subheader("📌 Condições Obrigatórias de Seleção (Pré-Live)")
st.markdown("""
Antes de seguires qualquer jogo, garante que ele cumpre estes **3 critérios estritos**:
1. 🏟️ **Fator Casa:** A equipa favorita joga obrigatoriamente no seu próprio estádio.
2. 📈 **Odds de Abertura:** A odd inicial para a vitória do visitado (1) está estritamente entre **1.20 e 1.45** (Ajustado para o mercado real).
3. 🏆 **Teste da Classificação:** O favorito está no **Top 4** da tabela e o adversário está na metade inferior.
""")
st.markdown("---")

# 2. CALCULADORA LIVE (MINUTO 55-60)
st.subheader("⚡ Validação de Massacre Real (SofaScore / FlashScore)")
st.markdown("Chegou o **minuto 55-60** e o jogo continua **0-0**? Confirma as estatísticas e marca com um **certo (✓)**:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📊 Estatísticas de Volume:")
    criterio_remates = st.checkbox("O favorito tem pelo menos 2 ou 3 'Remates à baliza'? (Ver na aba 'Estatísticas' do SofaScore ou Flashscore)")
    criterio_chances = st.checkbox("O favorito já criou 1 ou 2 'Grandes oportunidades'? (Ver na aba 'Estatísticas' do SofaScore ou Flashscore)")
    
with col2:
    st.markdown("#### 👁️ Leitura Visual do Gráfico:")
    grafico_sufoco = st.checkbox("O gráfico mostra barras altas do favorito coladas ao topo nos últimos 10 minutos? (Ver gráfico 'Momento do ataque' no SofaScore ou 'Desempenho ao vivo' na Flashscore)")

st.markdown("---")

# 3. VEREDITO FINAL DA FERRAMENTA
st.subheader("📢 Veredito da Ferramenta:")

# O sinal verde só dispara se todos os 3 critérios reais forem validados com "certo"
criterios_validos = (
    criterio_remates and 
    criterio_chances and 
    grafico_sufoco
)

if criterios_validos:
    st.error("""🚨 **ENTRADA APROVADA (BACK FAVORITO)** 🚨

• **Ação na OrbitX:** Colocar a tua Stake Fixa a favor do favorito (Back).
• **Plano de Saída:** Fazer Cash Out imediato assim que surgir o 1-0 para trancar o lucro.
• **Stop Loss:** Se continuar 0-0 ao minuto 78-80, fazer Cash Out na OrbitX e aceitar o red parcial.""")
else:
    st.warning("""⚠️ **AGUARDAR / NÃO ENTRAR** ⚠️

Garante que todos os critérios de massacre acima estão marcados com um certo (✓). Se faltar apenas um, o jogo não tem valor e não deves arriscar o teu dinheiro.""")
