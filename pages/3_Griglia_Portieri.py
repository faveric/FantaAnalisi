# import streamlit as st
# import os
# import pandas as pd
# import openpyxl
# import matplotlib.pyplot as plt
# import seaborn as sns
from functions import *


st.set_page_config(
    page_title="Griglia Portieri",
    page_icon="	:gloves:",
)

if st.session_state['use_custom']:
    st.sidebar.write(f"File quotazioni aggiornato manualmente in questa sessione.")
else:
    st.sidebar.write(f"Ultimo aggiornamento file quotazioni: {datetime.fromtimestamp(os.path.getmtime(st.session_state['prices_path']))}.")
# Load the data
data_dir = "./Data"
port_path = os.path.join(data_dir, "port.xlsx")

# Initialize session state for dataframe
if 'showall' not in st.session_state:
    st.session_state['showall'] = True

@st.cache_data
def load_data(path):
    # Read the data from the second row and first column onwards
    df = pd.read_excel(path, skiprows=1, index_col=0)
    return df


df = load_data(port_path)

# Streamlit application
st.title("Analisi Griglia Portieri")
st.write("Statisticamente i goal subiti in casa in Serie A sono inferiori ai goal subiti fuori casa. È consigliabile accoppiare i portieri in modo da averne almeno uno che gioca in casa per ogni giornata.")
st.write("La pagina può essere usata durante l'asta per valutare gli accoppiamenti migliori residui disponibili rimuovendo il flag dalle squadre il cui portiere titolare è stato già assegnato.")
# Filter by Squadra
st.header('Mostra/Nascondi Squadre')

buttons = st.columns(2)
def showall():
    st.session_state['showall'] = True
    return

def hideall():
    st.session_state['showall'] = False
    return

buttons[0].button('Mostra tutte', on_click=showall)
buttons[1].button('Nascondi tutte', on_click=hideall)


# Initialize a list of columns for checkboxes
checks = []

# Create 4 sets of columns with 5 columns each
for k in range(4):
    checks.append(st.columns(5))

# Add checkboxes for each squadra
checkboxes = {}
for i, squadra in enumerate(df.index):
    col_idx = i % 5
    row_idx = i // 5
    checkboxes[squadra] = checks[row_idx][col_idx].checkbox(squadra, value = st.session_state['showall'])

# Display the selected squadre
squadra_filter = [squadra for squadra, checked in checkboxes.items() if checked]
filtered_df = df.loc[squadra_filter]


# Apply the color map to the DataFrame

styled_df = filtered_df.style.background_gradient(
    cmap = 'RdYlGn_r',
    axis= None,
#    low = df.values.min(),
#    high = df.values.max()
).format('{:.0f}')

# Set  number format
pd.options.display.float_format = '{:,.0f}'.format

# Show Dataframe
st.dataframe(styled_df)

st.header('Migliori Accoppiamenti Disponibili')
# Create a set to store unique matchups
unique_matchups = set()

# Populate the set with sorted pairs
for team1 in filtered_df.index:
    for team2 in filtered_df.columns:
        if team2 in filtered_df.index:
            # Create a normalized tuple where the smaller team name comes first
            normalized_pair = tuple(sorted((team1, team2)))
            unique_matchups.add(normalized_pair)

# Create a DataFrame to store matchups with values from the original DataFrame
matchup_values = {
    pair: filtered_df.loc[pair[0], pair[1]] for pair in unique_matchups
}

# Convert the dictionary to a DataFrame
all_matchups = pd.DataFrame(list(matchup_values.items()), columns=['Matchup', 'Value'])

# Reset index
all_matchups.set_index('Matchup', inplace=True)

# Drop Same Team Coupling
all_matchups.dropna(inplace=True)
# Sort Couplings
all_matchups.sort_values('Value', ascending=True, inplace=True)

# Show dataframe
st.dataframe(all_matchups.style.format({2: '{:.0f}'}, precision=0, na_rep='MISS'))

print(st.session_state)
