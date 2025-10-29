
import pandas as pd
import matplotlib.pyplot as plt

# Dados de bairros
dados = {
    'bairro': ['Pinheiros', 'Vila Mariana', 'Itaquera', 'Moema', 'Santana'],
    'populacao': [65000, 130000, 220000, 90000, 110000],
    'latitude': [-23.5673, -23.5881, -23.5275, -23.6025, -23.4867],
    'longitude': [-46.6930, -46.6323, -46.4641, -46.6613, -46.6246]
}

df = pd.DataFrame(dados)

# Gráfico de dispersão simulando o mapa
plt.figure(figsize=(6,5))
plt.scatter(df['longitude'], df['latitude'], s=df['populacao']/1000, c='red', alpha=0.6)
plt.title('Mapa de bairros - São Paulo (escala por população)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Gráfico de barras
plt.figure(figsize=(6,4))
plt.bar(df['bairro'], df['populacao'], color='skyblue')
plt.title('População estimada por bairro')
plt.ylabel('Habitantes')
plt.show()
