# import streamlit as st
# import os
from functions import *

# Upload custom prices file
st.set_page_config(
    page_title="Aggiorna Lista Quotazioni",
    page_icon=":arrow_up_small:",
)

# Define paths
data_dir = "./Data"
prices_path = os.path.join(data_dir, "prices.xlsx")
stats_path = os.path.join(data_dir, "stats.xlsx")

# Use cache to reduce load time

# Define page
st.title("Aggiorna file delle quotazioni manualmente")
st.write('Puoi aggiornare il file delle quotazioni manualmente scaricando da https://www.fantacalcio.it/quotazioni-fantacalcio e caricando il file qui di seguito.')
new_file = st.file_uploader("Inserisci un file quotazioni aggiornato",
                                                     type=["xlsx"])
if new_file:
    # Load the uploaded file instead of the application list
    st.session_state['uploaded_file'] = new_file
    st.session_state['use_custom'] = True
    st.session_state['df'] = create_datafame(stats_path,
                                             prices_path,
                                             st.session_state['use_custom'],
                                             st.session_state['uploaded_file'])
    df_with_slots = create_slots(st.session_state['df'],
                                 st.session_state['num_participants'],
                                 st.session_state['slot_counts'],
                                 st.session_state['weights'])

    st.session_state['df'] = df_with_slots.reset_index(drop=True).set_index('Id').copy()

if st.session_state['use_custom']:
    st.sidebar.write(f"File quotazioni aggiornato manualmente in questa sessione.")
else:
    st.sidebar.write(f"Ultimo aggiornamento file quotazioni: {datetime.fromtimestamp(os.path.getmtime(st.session_state['prices_path']))}.")