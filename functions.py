import streamlit as st
import pandas as pd
import os
# import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from datetime import datetime
# import seaborn as sns
import requests
from bs4 import BeautifulSoup
import re


@st.cache_data
@st.cache_resource

# Function to load Excel file
def load_file(path):
    try:
        if os.path.exists(path):
            return pd.read_excel(path, skiprows=1, engine='openpyxl')
        else:
            st.error(f"File {path} non trovato, per favore carica una lista quotazioni")
            return pd.DataFrame()  # Return empty DataFrame if file not found
    except Exception as e:
        st.error(f"Errore nel caricamento del file {path}: {e}")
        return pd.DataFrame()  # Return empty DataFrame if an error occurs

def create_datafame(stats_path, prices_path, use_custom, uploaded_file):
    # Load data files
    stats_df = load_file(stats_path)
    if use_custom:
        prices_df = pd.read_excel(uploaded_file, skiprows=1, engine='openpyxl')
    else:
        prices_df = load_file(prices_path)

    # Ensure data is loaded
    if stats_df.empty or prices_df.empty:
        st.error('Errore nel caricamento dei file')
        st.stop()

    # Merge dataframes
    merged_df = pd.merge(prices_df, stats_df, on="Id", how="left", suffixes=('', '_right')).fillna(0)

    # Drop columns from the right DataFrame if names overlap with the left DataFrame
    for col in merged_df.columns:
        if col.endswith('_right'):
            original_col = col.rsplit('_', 1)[0]
            if original_col in merged_df.columns:
                merged_df.drop(columns=[col], inplace=True)

    # Create a column for new arrivals
    mask_new = ~merged_df['Id'].isin(stats_df['Id'])
    merged_df['Nuovo'] = mask_new

    return merged_df

# Function to create slots
def create_slots(df, num_participants, slot_counts, weights):
    players_per_slot = num_participants
    df_per_role = []
    for role in slot_counts.keys():
        slot_count = slot_counts[role]
        df_sorted = df[df["R"] == role].copy()
        df_sorted.loc[:,'SCORE'] = weight_function(df_sorted, weights)
        df_sorted = df_sorted.sort_values(by="SCORE", ascending=False).reset_index(drop=True)
        df_sorted.loc[:,'SLOT'] = 99
        for i in range(0,slot_count):
            df_sorted.loc[i * players_per_slot:(i + 1) * players_per_slot, 'SLOT'] = i + 1
        df_per_role.append(df_sorted)
    df_with_slots = pd.concat(df_per_role)
    # Reorder columns to bring 'SLOT' and 'SCORE' to the front
    columns = ['SLOT', 'SCORE'] + [col for col in df_with_slots.columns if col not in ['SLOT', 'SCORE']]
    df_with_slots = df_with_slots[columns]
    return df_with_slots

def weight_function(df, weights):
    df_cp=df.copy()
    max_0 = df_cp['Qt.A'].max()
    max_1 = df_cp['Fm'].max()
    max_2 = df_cp['Pv'].max()
    min_0 = df_cp['Qt.A'].min()
    min_1 = df_cp['Fm'].min()
    min_2 = df_cp['Pv'].min()
    F0 = (df_cp['Qt.A']-min_0)/(max_0-min_0)
    F1 = (df_cp['Fm']-min_1)/(max_1-min_1)
    F2 = (df_cp['Pv']-min_2)/(max_2-min_2)
    df_cp.loc[:,'SCORE'] = F0*weights[0] + F1*weights[1] + F2*weights[2]
    return df_cp.loc[:,'SCORE']

def reset_quotazioni():
    st.session_state['use_custom'] = False


def create_radar_chart(df, legend_column, max_vals=pd.DataFrame()):
    # Identify max values
    if max_vals.empty:
        max_vals = df.max()

    # Identify the categories for the radar chart
    categories = [col for col in df.columns if ((col != 'index') and
                                                (col != 'Nome') and
                                                (col != 'SLOT') and
                                                (col != 'SCORE') and
                                                (col != legend_column))]

    # Extract colors from the 'Reds' colormap
    colormap = plt.get_cmap('Reds')
    n_colors = len(df.index)

    # Generate colors from the colormap and convert from RGBA to HEX
    colors = [mcolors.to_hex(colormap(i / n_colors)) for i in range(n_colors)]

    fig = go.Figure()

    # Normalize data
    df_normalized = df.copy()
    for col in categories:
        max_value = max_vals[col] #df[col].max()
        df_normalized[col] = df[col] / max_value if max_value != 0 else df[col]

    for idx, element in enumerate(df.index):
        values = df_normalized.loc[element, categories].values
        legend_name = df.loc[element, legend_column]
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=f'{legend_name}',
            line=dict(color=colors[-1-idx])  # Apply color from the color map
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]  # Since we normalized to 0-1, the range is [0, 1]
            ),
            angularaxis=dict(
                tickvals=[i for i in range(len(categories))],
                ticktext=categories,
                tickmode='array'
            ),
        ),
        showlegend=True,
        legend=dict(
            title=legend_column,  # Title for the legend
            title_font=dict(size=14),  # Font size for the title
            xanchor='left',
            yanchor='top',
            x=1.05,  # Adjust this value to position the legend title
            y=1.05   # Adjust this value to position the legend title
        )
    )

    return fig

def show_summary(df, legend_column, max_vals=pd.DataFrame()):
    cols = st.columns(2, vertical_alignment='center')
    with cols[0]:
        st.dataframe(df.style.background_gradient(cmap='Reds', gmap=df['SCORE']))
    with cols[1]:
        st.plotly_chart(create_radar_chart(df, legend_column, max_vals), use_container_width=True)

def show_summary_players(df, legend_column, max_vals=pd.DataFrame()):
    df_subset = df[["SLOT", "SCORE", "Nome", "Qt.A", "Mv", "Fm", "Gf", "Ass", "Pv"]].copy()
    st.dataframe(df.style.background_gradient(cmap='Reds', gmap=df['SCORE']))
    st.plotly_chart(create_radar_chart(df_subset, legend_column, max_vals), use_container_width=True)

def player_description_webfetch(player_data):
    # URL of the webpage
    teams = player_data['Squadra']
    ids = player_data.index

    # Create a dictionary of URLs
    urls = {id: f"https://www.fantacalcio.it/serie-a/squadre/{team}/{team}/{id}" for id, team in zip(ids, teams)}

    # Dictionary to store descriptions
    descriptions = {}

    # Send HTTP requests and parse the content for each URL
    for id, url in urls.items():
        try:
            # Send an HTTP request to the website
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(response.content, 'html.parser')

                # Extract the player description section by its ID
                description_section = soup.find('section', id='player-description')

                # Extract the paragraphs inside the section if it exists
                if description_section:
                    paragraphs = description_section.find_all('p')

                    # Filter out empty or spaces-only paragraphs
                    desc = []
                    for p in paragraphs:
                        text = p.get_text().strip()
                        if text:
                            desc.append(text)

                    # Store the joined description for the current player ID
                    descriptions[id] = '\n'.join(desc)
                else:
                    descriptions[id] = None  # If no description found
            else:
                descriptions[id] = None  # If the request failed
        except Exception as e:
            descriptions[id] = None  # Handle any exceptions

    # Create a DataFrame with 'Id' as index and 'description' as the column
    description_df = pd.DataFrame.from_dict(descriptions, orient='index', columns=['description'])

    return description_df
def player_description_live(player_data):
    # URL of the webpage
    team = player_data['Squadra'].iloc[0]
    id = player_data.index[0]
    st.subheader(f"{player_data['Nome'].iloc[0]}")
    url = f"https://www.fantacalcio.it/serie-a/squadre/{team}/{team}/{id}"

    # Send an HTTP request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the player description section by its ID
        # Extract the player description section by its ID
        description_section = soup.find('section', id='player-description')

        # Extract the paragraphs inside the section if it exists
        if description_section:
            # Extract all <p> tags inside the description section (ignoring empty or irrelevant ones)
            paragraphs = description_section.find_all('p')

            # Filter out paragraphs with text only, ignore empty or spaces-only paragraphs
            #description_text = '\n'.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
            for p in paragraphs:
                text = p.get_text().strip()
                if text:
                    st.write(p.get_text().strip())

        # Output the extracted text

        #st.write(description_text)
    else:
        st.write(f"Failed to retrieve content. Status code: {response.status_code}")

def player_description(descriptions_df, player_data):
    player_desc = descriptions_df[descriptions_df['Id'] == player_data.index[0].astype('int')]['description'].iloc[0]

    # Split the text based on the section labels
    sections = re.split(r'(?=Statistiche anno|Gestione al Fantacalcio|Note positive|Note negative)', player_desc)

    # Remove any leading/trailing whitespace from each section
    sections = [section.strip() for section in sections if section.strip()]

    for sec in sections:
        st.write(sec)
