# import streamlit as st
from functions import *

# Upload custom prices file
st.set_page_config(
    page_title="Consulta Lista Quotazioni",
    page_icon=":soccer:",
)

if st.session_state['use_custom']:
    st.sidebar.write(f"File quotazioni aggiornato manualmente in questa sessione.")
else:
    st.sidebar.write(f"Ultimo aggiornamento file quotazioni: {datetime.fromtimestamp(os.path.getmtime(st.session_state['prices_path']))}.")
# Page Title
st.title('Consulta Lista Quotazioni')
st.write('Consulta la lista delle quotazioni! Sulla barra di sinistra puoi applicare dei filtri, la lista contiene anche le statistiche della stagione 2023/2024')
# Title Sidebar
st.sidebar.title('Filtri')
# Sidebar filters
R = st.sidebar.multiselect("Ruolo (R)", st.session_state['df']["R"].unique())
Squadra = st.sidebar.multiselect("Squadra", st.session_state['df']["Squadra"].unique())

# Filtered DataFrame based on sidebar selections
filtered_df = st.session_state['df'].copy()
if R:
    filtered_df = filtered_df[filtered_df["R"].isin(R)]
if Squadra:
    filtered_df = filtered_df[filtered_df["Squadra"].isin(Squadra)]

Nome = st.sidebar.multiselect("Nome", filtered_df["Nome"].unique())
QtA_min = st.sidebar.number_input("Qt.A Min", value=0.0, step=1.0)
QtA_max = st.sidebar.number_input("Qt.A Max", value=100.0, step=1.0)
Mv_min = st.sidebar.number_input("Mv Min", value=0.0, step=0.5)
Mv_max = st.sidebar.number_input("Mv Max", value=10.0, step=0.5)
Fm_min = st.sidebar.number_input("Fm Min", value=0.0, step=0.5)
Fm_max = st.sidebar.number_input("Fm Max", value=15.0, step=0.5)

# Apply numerical filters
filtered_df = filtered_df[
    (filtered_df["Qt.A"] >= QtA_min) & (filtered_df["Qt.A"] <= QtA_max) &
    (filtered_df["Mv"] >= Mv_min) & (filtered_df["Mv"] <= Mv_max) &
    (filtered_df["Fm"] >= Fm_min) & (filtered_df["Fm"] <= Fm_max)
]

# Apply name filter if selected
if Nome:
    filtered_df = filtered_df[filtered_df["Nome"].isin(Nome)]

#filtered_df = filtered_df.reset_index(drop=True).set_index('Id')

st.dataframe(filtered_df.style.background_gradient(cmap='Reds', gmap=st.session_state['df']['SCORE']))

print(st.session_state)