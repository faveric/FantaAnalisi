from functions import *
player_data=pd.DataFrame({
    'id':[5876],
    'Nome' :  ['Di Gregorio'],
    'Squadra': ['Juventus']
}).set_index('id')

print(player_data)

player_description(player_data)
