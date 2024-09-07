# import streamlit as st
# import pandas as pd
# import os
# import matplotlib.pyplot as plt
# import seaborn as sns

from functions import *

st.set_page_config(
    page_title="FantaAnalisi",
    page_icon="	:soccer:",
)

# Define paths
data_dir = "./Data"
prices_path = os.path.join(data_dir, "prices.xlsx")
stats_path = os.path.join(data_dir, "stats.xlsx")
desc_path = os.path.join(data_dir, "descriptions.csv")

@st.cache_data
def load_descriptions(path):
    descriptions = pd.read_csv(path)
    return descriptions

descriptions_df = load_descriptions(desc_path)
# @st.cache_resource

# Title
st.title('FantaAnalisi')
st.write("Analisi fantacalcistiche per realizzare l'asta perfetta!")


# Session States
if 'use_custom' not in st.session_state:
    st.session_state['use_custom'] = False
if 'showall' not in st.session_state:
    st.session_state['showall'] = True
if 'weights' not in st.session_state:
    st.session_state['weights'] = [0.7, 0.2, 0.1]
if 'num_participants' not in st.session_state:
    st.session_state['num_participants'] = 8
# Define slot counts for each role
if 'slot_counts' not in st.session_state:
    st.session_state['slot_counts'] = {'P': 3, 'D': 8, 'C': 8, 'A': 6}
if 'uploaded_file' not in st.session_state:
    st.session_state['uploaded_file'] = None
if 'prices_path' not in st.session_state:
    st.session_state['prices_path'] = prices_path

if st.sidebar.button('ripristina quotazioni'):
    reset_quotazioni()

st.session_state['df'] = create_datafame(stats_path, prices_path, st.session_state['use_custom'], st.session_state['uploaded_file'])

# Slots Calculation and Visualization
st.header("Configurazione Analisi Asta per Slot", divider='red')
st.write("""
La sezione seguente consente di raggruppare i giocatori della lista quotazioni per **SLOT** in base al numero di partecipanti all'asta. 

Ogni slot contiene un numero di giocatori pari al numero di partecipanti, ordinati per SCORE. 

L'idea è che ogni partecipante cercherà di acquistare i giocatori con lo **SCORE** più alto, quindi l'asta procederà presumibilmente in ordine di slot.

I calciatori in lista eccedenti il numero di slot previsto per ogni ruolo vengono convenzionalmente assegnati allo slot n°99.
""")

st.session_state['num_participants'] = st.number_input("Numero di Partecipanti Asta", min_value=2, value=8)

st.write("""
Lo SCORE viene calcolato come media pesata dei valori normalizzati dell quotazione attuale, della FantaMedia e del numero di presenze.

L'attribuzione dei pesi può essere personalizzata dall'utente.
""")

# Assign weights for slot definition
weights=st.columns(3)
st.session_state['weights'][0] = weights[0].number_input('Peso Quotazione Attuale', min_value=0.0, max_value=1.0, value=0.7, step=0.05)
st.session_state['weights'][1] = weights[1].number_input('Peso FMV precedente stagione', min_value=0.0, max_value=1.0, value=0.2, step=0.05)
st.session_state['weights'][2] = weights[2].number_input('Peso Presenze precedente stagione', min_value=0.0, max_value=1.0, value=0.1, step=0.05)
if round(sum(st.session_state['weights']),2) != 1.0:
    st.warning('La somma dei pesi deve essere uguale a 1')


# Create and display slots
df_with_slots = create_slots(st.session_state['df'],
                             st.session_state['num_participants'],
                             st.session_state['slot_counts'],
                             st.session_state['weights'])

st.session_state['df'] = df_with_slots.reset_index(drop=True).set_index('Id').copy()

st.header('Analisi Slot', divider='red')
players = df_with_slots[df_with_slots['R'].isin(['D', 'C', 'A'])][["R", "SLOT", "SCORE", "Qt.A", "Mv", "Fm", "Gf", "Ass", "Pv"]].copy()
gks = df_with_slots[df_with_slots['R'].isin(['P'])][["SLOT", "SCORE", "Qt.A", "Mv", "Fm",  "Gs", "Rp", "Pv"]].copy()
dfs = players[players['R']=='D'][["SLOT", "SCORE", "Qt.A", "Mv", "Fm", "Gf", "Ass", "Pv"]].copy()
cns = players[players['R']=='C'][["SLOT", "SCORE", "Qt.A", "Mv", "Fm", "Gf", "Ass", "Pv"]].copy()
ats = players[players['R']=='A'][["SLOT", "SCORE", "Qt.A", "Mv", "Fm", "Gf", "Ass", "Pv"]].copy()
gks_summary = gks.groupby('SLOT').mean().reset_index()
dfs_summary = dfs.groupby('SLOT').mean().reset_index()
cns_summary = cns.groupby('SLOT').mean().reset_index()
ats_summary = ats.groupby('SLOT').mean().reset_index()

# Display slots and summary statistics
st.subheader('Medie per slot Portieri')
show_summary(gks_summary, 'SLOT')
st.subheader('Medie per slot Difensori')
show_summary(dfs_summary, 'SLOT')
st.subheader('Medie per slot Centrocampisti')
show_summary(cns_summary, 'SLOT')
st.subheader('Medie per slot Attaccanti')
show_summary(ats_summary, 'SLOT')

st.header('Visualizza Slot', divider='red')
role = st.selectbox('Ruolo', ('P', 'D', 'C', 'A'))
slot_num = st.selectbox('Slot', df_with_slots[df_with_slots['R']==role]['SLOT'].unique())

selected_slot = df_with_slots[(df_with_slots['R']==role) & df_with_slots['SLOT'].isin([slot_num])]
max_vals = df_with_slots[(df_with_slots['R']==role)][["SLOT", "SCORE", "Qt.A", "Mv", "Fm", "Gf", "Ass", "Pv"]].max()
show_summary_players(selected_slot, 'Nome', max_vals)

# Player Comparison
st.header("Confronto Giocatori", divider='red')
player1 = st.selectbox("Giocatore 1", st.session_state['df']["Nome"].unique())
player2 = st.selectbox("Giocatore 2", st.session_state['df']["Nome"].unique())

player1_data = st.session_state['df'][st.session_state['df']["Nome"] == player1]
player2_data = st.session_state['df'][st.session_state['df']["Nome"] == player2]
players_confronto = st.session_state['df'][st.session_state['df']["Nome"].isin([player1, player2])]

max_vals_confronto = df_with_slots[["SLOT", "SCORE", "Qt.A", "Mv", "Fm", "Gf", "Ass", "Pv"]].max()
show_summary_players(players_confronto, 'Nome', max_vals_confronto)


st.subheader(f"{player1_data['Nome'].iloc[0]}")
player_description(descriptions_df, player1_data)
st.subheader(f"{player2_data['Nome'].iloc[0]}")
player_description(descriptions_df, player2_data)

if st.session_state['use_custom']:
    st.sidebar.write(f"File quotazioni aggiornato manualmente in questa sessione.")
else:
    st.sidebar.write(f"Ultimo aggiornamento file quotazioni: {datetime.fromtimestamp(os.path.getmtime(st.session_state['prices_path']))}.")
