from html import escape

import pandas as pd
from folium import GeoJson, Icon, LayerControl, Map, Marker, Popup
from folium.plugins import FeatureGroupSubGroup, MarkerCluster

EXCEL_FILE = 'География_устройства.xlsx'
GEOJSON_FILE = 'map.geojson'
OUTPUT_FILE = 'map.html'

REQUIRED_COLUMNS = ['Устройство', 'Город', 'Адрес', 'Режим работы', 'Широта', 'Долгота']

# Цвет и иконка метки для каждого типа устройства
DEVICE_STYLES = {
    'Банкомат': {'color': 'blue', 'icon': 'credit-card'},
    'Терминал': {'color': 'green', 'icon': 'cash-register'},
}
DEFAULT_STYLE = {'color': 'gray', 'icon': 'circle-info'}


def load_devices(path=EXCEL_FILE):
    df = pd.read_excel(path)
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f'В файле {path} нет столбцов: {", ".join(missing)}')
    return df


def popup_html(device):
    return (
        f"<b>{escape(device['Устройство'])}</b><br>"
        f"{escape(device['Адрес'])}<br>"
        f"{escape(device['Режим работы'])}"
    )


def build_map(df=None):
    if df is None:
        df = load_devices()

    m = Map(location=[df['Широта'].mean(), df['Долгота'].mean()], zoom_start=5)

    # Граница Казахстана: контур с почти прозрачной заливкой
    GeoJson(
        GEOJSON_FILE,
        name='Граница Казахстана',
        style_function=lambda _: {'color': '#3388ff', 'weight': 2, 'fillOpacity': 0.05},
    ).add_to(m)

    # Один общий кластер и внутри него слой для каждого типа устройства:
    # типы можно включать и выключать, а кластеры остаются общими
    cluster = MarkerCluster(control=False).add_to(m)
    layers = {
        name: FeatureGroupSubGroup(cluster, name=name).add_to(m)
        for name in df['Устройство'].unique()
    }

    for device in df.to_dict('records'):
        style = DEVICE_STYLES.get(device['Устройство'], DEFAULT_STYLE)
        Marker(
            [device['Широта'], device['Долгота']],
            popup=Popup(popup_html(device), max_width=300),
            tooltip=f"{device['Устройство']}, {device['Город']}",
            icon=Icon(color=style['color'], icon=style['icon'], prefix='fa'),
        ).add_to(layers[device['Устройство']])

    LayerControl(collapsed=False).add_to(m)
    m.fit_bounds([
        [df['Широта'].min(), df['Долгота'].min()],
        [df['Широта'].max(), df['Долгота'].max()],
    ])
    return m


if __name__ == '__main__':
    build_map().save(OUTPUT_FILE)
    print(f'Карта сохранена в {OUTPUT_FILE}')
