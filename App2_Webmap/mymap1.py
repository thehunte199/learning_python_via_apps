import folium
import pandas

map = folium.Map(location=[35.54, -78.54], zoomtiles="Stamen Terrain")
feat_group_volcs = folium.FeatureGroup(name="Volcanoes")

data = pandas.read_csv("./Volcanoes.txt")
lats = list(data["LAT"])
lons = list(data["LON"])
names = list(data["NAME"])
elevs =  list(data["ELEV"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elev):
    color = 'white'
    if elev is not None and elev > 0:
        if elev < 1000:
            color = 'green'
        elif elev < 2000:
            color = 'orange'
        elif elev < 3000:
            color = 'red'
        else:
            color = 'black'
    return color    

for lat, lon, name, elev in zip(lats, lons, names, elevs):
    iframe = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    feat_group_volcs.add_child(folium.Marker(location=(lat, lon), popup=folium.Popup(iframe), icon=folium.Icon(color_producer(elev))))    

feat_group_pop = folium.FeatureGroup(name="Population")

feat_group_pop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(feat_group_volcs)
map.add_child(feat_group_pop)
map.add_child(folium.LayerControl())
map.save("./MyMap1.html")