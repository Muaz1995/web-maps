import folium
import pandas

data = pandas.read_csv("volcanos.txt")
lat = list(data["LAT"]) # This is a list with all the latitudinal values from volcanos.txt
lon = list(data["LON"]) #This is a list with all the longitudinal values from volcanos.txt
elev = list(data["ELEV"]) #This is a list with all the elevation values from volcanos.txt

def color_producer(el):
        if el < 1000:
                return 'green'
        elif 1000 <= el < 3000:
                return 'purple'
        else:
                return 'red'
map = folium.Map(location=[38.58,-99.09],zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanos") 

for lt, ln, el in zip(lat, lon, elev):
        fgv.add_child(folium.CircleMarker(location= [lt,ln],radius = 10, popup = str(el) + "m",
        fill_color = color_producer(el),color = 'grey',fill_opacity = 0.7 ))

fgp = folium.FeatureGroup(name="Population") # Feature group to use for layer control on line 33     

world = r'C:\Users\USER\Desktop\mapping\extract me json.zip\world.json'
fgp.add_child(folium.GeoJson(data=open(world,'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) # This adds a color to the map which is yellow

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
