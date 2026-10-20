# Device Map of Kazakhstan

**EN** · [RU](#карта-устройств-казахстана)

An interactive map of ATMs and payment terminals in Kazakhstan. The list of devices comes from an Excel file: 94 devices (61 ATMs and 33 terminals) with city, address, opening hours and coordinates. The map shows the country border, groups nearby devices into clusters and lets you switch ATMs and terminals on and off.

**Files**
- `index.ipynb` - notebook to view the map in Jupyter.
- `index.py` - the map code. Run it as a script to save the map to `map.html`.
- `География_устройства.xlsx` - device list. Required columns: `Устройство`, `Город`, `Адрес`, `Режим работы`, `Широта`, `Долгота`.
- `map.geojson` - Kazakhstan border.

**How to run**

Install the libraries once (for example, in Anaconda Prompt):
```
pip install -r requirements.txt
```

In Jupyter: open `index.ipynb` and run the cell (Shift+Enter). If you see "Make this Notebook Trusted to load map" instead of the map, choose File → Trust Notebook.

Without Jupyter: run `python index.py` in the project folder and open the created `map.html` in a browser.

To update the map, change the Excel file and run it again. If `index.py` was changed while the notebook is open, restart the kernel first (Kernel → Restart).

**Stack:** Python, pandas, folium (Leaflet), Jupyter.

---

## Карта устройств Казахстана

[EN](#device-map-of-kazakhstan) · **RU**

Интерактивная карта банкоматов и платёжных терминалов в Казахстане. Список устройств берётся из Excel-файла: 94 устройства (61 банкомат и 33 терминала) с городом, адресом, режимом работы и координатами. На карте видна граница страны, близкие устройства объединяются в кластеры, а банкоматы и терминалы можно включать и выключать.

**Файлы**
- `index.ipynb` - ноутбук для просмотра карты в Jupyter.
- `index.py` - код карты. Если запустить его как скрипт, карта сохранится в `map.html`.
- `География_устройства.xlsx` - список устройств. Обязательные столбцы: `Устройство`, `Город`, `Адрес`, `Режим работы`, `Широта`, `Долгота`.
- `map.geojson` - граница Казахстана.

**Как запустить**

Один раз установить библиотеки (например, в Anaconda Prompt):
```
pip install -r requirements.txt
```

В Jupyter: открыть `index.ipynb` и запустить ячейку (Shift+Enter). Если вместо карты видна надпись «Make this Notebook Trusted to load map», выбрать File → Trust Notebook.

Без Jupyter: в папке проекта выполнить `python index.py` и открыть созданный `map.html` в браузере.

Чтобы обновить карту, достаточно изменить Excel-файл и запустить заново. Если `index.py` менялся при открытом ноутбуке, сначала перезапустить ядро (Kernel → Restart).

**Стек:** Python, pandas, folium (Leaflet), Jupyter.
