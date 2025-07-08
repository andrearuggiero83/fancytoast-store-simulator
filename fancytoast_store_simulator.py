
import streamlit as st

st.set_page_config(page_title="Fancytoast Store Simulator", layout="centered")

st.title("🥪 Fancytoast Store Simulator")
st.markdown("Simula la sostenibilità economica del punto vendita un punto vendita Fancytoast.")

st.header("📥 Parametri di input")

col1, col2 = st.columns(2)

with col1:
    coperti_feriali = st.number_input("Coperti feriali", value=100, min_value=0)
    giorni_feriali = st.number_input("Giorni feriali", value=260, min_value=0)
    scontrino_feriali = st.number_input("Scontrino medio feriali (€)", value=13.5, min_value=0.0)

    canone_fisso = st.number_input("Canone fisso annuo (€)", value=90000)
    spese_accessorie = st.number_input("Spese accessorie annue (€)", value=8565)
    food_cost_perc = st.slider("Food cost %", 10, 50, value=30)

with col2:
    coperti_weekend = st.number_input("Coperti weekend", value=60, min_value=0)
    giorni_weekend = st.number_input("Giorni weekend", value=103, min_value=0)
    scontrino_weekend = st.number_input("Scontrino medio weekend (€)", value=14.0, min_value=0.0)

    percentuale_complementare = st.slider("Complementare % su fatturato", 0, 20, value=10)
    labor_cost_perc = st.slider("Labor cost %", 10, 50, value=32)
    opex_perc = st.slider("OPEX %", 5, 20, value=10)
    royalty_perc = st.slider("Royalty + HQ %", 0, 10, value=6)

# Calcoli
ricavi_feriali = coperti_feriali * scontrino_feriali * giorni_feriali
ricavi_weekend = coperti_weekend * scontrino_weekend * giorni_weekend
ricavi_totali = ricavi_feriali + ricavi_weekend

affitto_complementare = ricavi_totali * percentuale_complementare / 100
affitto_totale = canone_fisso + affitto_complementare + spese_accessorie

food_cost = ricavi_totali * food_cost_perc / 100
labor_cost = ricavi_totali * labor_cost_perc / 100
opex = ricavi_totali * opex_perc / 100
royalty = ricavi_totali * royalty_perc / 100

ebitda = ricavi_totali - (affitto_totale + food_cost + labor_cost + opex + royalty)

st.header("📊 Risultati")

st.metric("Ricavi totali (€)", f"{ricavi_totali:,.0f}")
st.metric("Affitto totale (€)", f"{affitto_totale:,.0f}")
st.metric("EBITDA operativo (€)", f"{ebitda:,.0f}", delta_color="inverse" if ebitda < 0 else "normal")

with st.expander("📋 Dettaglio costi e margini"):
    st.write(f"Food cost: €{food_cost:,.0f}")
    st.write(f"Labor cost: €{labor_cost:,.0f}")
    st.write(f"OPEX: €{opex:,.0f}")
    st.write(f"Royalty + HQ: €{royalty:,.0f}")


st.header("📌 Valutazione finale")

if ebitda > 30000:
    st.success("✅ Operazione sostenibile: il punto vendita è economicamente valido con buona marginalità.")
elif 0 < ebitda <= 30000:
    st.warning("⚠️ Operazione potenzialmente sostenibile ma da ottimizzare: rivedere costi o negoziare canone.")
else:
    st.error("❌ Operazione non sostenibile: l'affitto o i costi fissi risultano troppo alti per i ricavi attesi.")
