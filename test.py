from functions import *


# Define paths
data_dir = "./Data"
prices_path = os.path.join(data_dir, "prices.xlsx")

# Read Ids
df = pd.read_excel(prices_path, skiprows=1, engine='openpyxl').set_index('Id')

# Read Descriptions from online resource
df['description'] = player_description_webfetch(df)

# Create description csv
df[['description']].to_csv(os.path.join(data_dir, "descriptions.csv"))