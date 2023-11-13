import pandas as pd
from folium import Map, Marker, GeoJson
from folium.plugins import MarkerCluster

# Путь к файлу Excel
excel_file_path = 'География_устройства.xlsx'
df = pd.read_excel(excel_file_path)

kz_lat, kz_lng = 48.0196, 66.9237
m = Map(location=[kz_lat, kz_lng], zoom_start=5)

# Путь к файлу GeoJSON
geojson_file_path = 'map.geojson'
geojson_layer = GeoJson(geojson_file_path, name='Kazakhstan Borders')
geojson_layer.add_to(m)

marker_cluster = MarkerCluster().add_to(m)

def create_clusters(row):
    Marker(
        [row['Широта'], row['Долгота']],
        popup=f"{row['Устройство']} {row['Адрес']}",
    ).add_to(marker_cluster)

df.apply(create_clusters, axis=1)

m