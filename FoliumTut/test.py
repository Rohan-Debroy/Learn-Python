import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
el=list(data["ELEV"])

def colourizer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[38,-99])
fg1=folium.FeatureGroup("Volcanoes Location in USA")
fg2=folium.FeatureGroup("Polygon Layer")
for lt, ln, name, el in zip(lat,lon,name,el):
    #fg1.add_child(folium.Marker(location=[lt,ln], popup=name, icon=folium.Icon(color=colourizer(el))))
    fg1.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=name, tooltip=str(el)+'m',
    fill_color=colourizer(el), color='grey',fill_opacity=0.7))

fg2.add_child(folium.GeoJson(data=open("world.json",'r',encoding="UTF-8-sig").read(), 
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map1.html")