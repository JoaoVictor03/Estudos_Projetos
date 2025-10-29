import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Dados simplificados de bairros de São Paulo
dados = {
    'bairro': ['Pinheiros', 'Vila Mariana', 'Itaquera', 'Moema', 'Santana'],
    'populacao': [65000, 130000, 220000, 90000, 110000],
    'latitude': [-23.5673, -23.5881, -23.5275, -23.6025, -23.4867],
    'longitude': [-46.6930, -46.6323, -46.4641, -46.6613, -46.6246]
}

df = pd.DataFrame(dados)

# Cria um GeoDataFrame
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326"
)

# --- Mapa de calor simples ---
fig, ax = plt.subplots(1, 2, figsize=(10,5))

# Mapa
gdf.plot(ax=ax[0], color='lightblue', edgecolor='black')
gdf.plot(ax=ax[0], column='populacao', cmap='Reds', legend=True)
ax[0].set_title('População por Bairro - São Paulo')
ax[0].set_xlabel('Longitude')
ax[0].set_ylabel('Latitude')

# Gráfico de barras
ax[1].bar(df['bairro'], df['populacao'], color='tomato')
ax[1].set_title('População estimada por bairro')
ax[1].set_xlabel('Bairro')
ax[1].set_ylabel('Habitantes')

plt.tight_layout()
plt.show()
