import pandas as pd

dfOriginal = df = pd.read_csv("solicitudes_credito.csv", sep=";") 
df = pd.read_csv("solicitudes_credito.csv", sep=";")
df.drop('Unnamed: 0', axis=1, inplace=True)
df.dropna(how='all')

df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# === Idea negocio


df = df.applymap(lambda x: x.replace('_', ' ').replace('-', ' ') if isinstance(x, str) else x)
#df.drop(df[df.idea_negocio.str.endswith('en ') | df.idea_negocio.str.endswith('de ')].index, inplace=True)
#df['barrio'] = df.barrio.str.replace('bel¿n', 'belen').str.replace('andaluc¿a', 'andalucia').str.replace('antonio nari¿o', 'antonio nariño').str.replace('campo vald¿s no.1', 'campo valdes no. 1').str.replace('boyac¿', 'boyaca')
df['fecha_de_beneficio']= pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True)
df['monto_del_credito'] = df['monto_del_credito'].str.extract('(\d+)', expand=False)
df['monto_del_credito'] = df['monto_del_credito'].astype(float)

df.drop_duplicates(inplace=True)
print(df)