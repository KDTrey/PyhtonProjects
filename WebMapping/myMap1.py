import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevate):
    if(elevate<1000):
        return 'green'
    elif(1000<= elevate <3000):
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[29.75, -95.38],zoom_start=8, tiles='Mapbox Bright')

fgv = folium.FeatureGroup(name='Volcanoes')#Adds a Volcano layer

#for loop that places markers on all the volcanoes in the US and has a popup that displays the elevation in meters
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=5, popup=str(el)+"m",color='gray', fill_color=color_producer(el), fill_opacity=0.7))

fgp = folium.FeatureGroup("Population")#Adds a population layer
#lambda function that assigns colors to countries based on population
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
