import pandas as pd

data = pd.read_excel('algoritm/Valladatamer.xlsx')

data = data.dropna(axis='columns')

# replace 'Snötyp:' and 'Valla (Label)' with 0,1,2,...
snow_to_label = {}
label_to_snow = {}

wax_to_label = {}
label_to_wax = {}

for i in data.index:
    if data.at[i, 'Snötyp:'] not in snow_to_label:
        snow_to_label[data.at[i, 'Snötyp:']] = len(snow_to_label)
        label_to_snow[len(label_to_snow)] = data.at[i, 'Snötyp:']
    
    data.at[i, 'Snötyp:'] = snow_to_label[data.at[i, 'Snötyp:']]

    if data.at[i, 'Valla (Label)'] not in wax_to_label:
        wax_to_label[data.at[i, 'Valla (Label)']] = len(wax_to_label)
        label_to_wax[len(label_to_wax)] = data.at[i, 'Valla (Label)']
    
    data.at[i, 'Valla (Label)'] = wax_to_label[data.at[i, 'Valla (Label)']]

data.to_csv('algoritm/Valladatamer_prep.csv', index=False)

label_to_wax_df = pd.DataFrame.from_dict(label_to_wax, orient='index')

label_to_wax_df.to_csv('algoritm/label_to_wax.csv', header=False)

snow_to_label_df = pd.DataFrame.from_dict(snow_to_label, orient='index')

snow_to_label_df.to_csv('algoritm/snow_to_label.csv', header=False)

# read the data
data = pd.read_excel('algoritm/Valladata.xlsx')

data = data.dropna(axis='columns')

# replace 'Snötyp:' and 'Valla (Label)' with 0,1,2,...
snow_to_label = {}
label_to_snow = {}

wax_to_label = {}
label_to_wax = {}

for i in data.index:
    if data.at[i, 'Snötyp:'] not in snow_to_label:
        snow_to_label[data.at[i, 'Snötyp:']] = len(snow_to_label)
        label_to_snow[len(label_to_snow)] = data.at[i, 'Snötyp:']
    
    data.at[i, 'Snötyp:'] = snow_to_label[data.at[i, 'Snötyp:']]

    if data.at[i, 'Valla (Label)'] not in wax_to_label:
        wax_to_label[data.at[i, 'Valla (Label)']] = len(wax_to_label)
        label_to_wax[len(label_to_wax)] = data.at[i, 'Valla (Label)']
    
    data.at[i, 'Valla (Label)'] = wax_to_label[data.at[i, 'Valla (Label)']]

data.to_csv('algoritm/Valladata_prep.csv', index=False)

label_to_wax_df = pd.DataFrame.from_dict(label_to_wax, orient='index')

label_to_wax_df.to_csv('algoritm/label_to_wax.csv', header=False)

snow_to_label_df = pd.DataFrame.from_dict(snow_to_label, orient='index')

snow_to_label_df.to_csv('algoritm/snow_to_label.csv', header=False)