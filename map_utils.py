import folium
from cities import graph

def plot_route(path, filename='route_map.html'):
    start_city = path[0]
    m = folium.Map(location=[graph[start_city]['lat'], graph[start_city]['lon']], zoom_start=7)
    coords = [(graph[c]['lat'], graph[c]['lon']) for c in path]
    folium.PolyLine(coords, color='red', weight=5, opacity=0.8).add_to(m)
    for c, (lat, lon) in zip(path, coords):
        folium.Marker(location=[lat, lon], popup=c).add_to(m)
    m.save(filename)
    return filename
