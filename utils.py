import math
import heapq
from cities import graph

def haversine_distance(city1, city2):
    R = 6371  # km
    lat1, lon1 = math.radians(city1["lat"]), math.radians(city1["lon"])
    lat2, lon2 = math.radians(city2["lat"]), math.radians(city2["lon"])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start, 0, None))
    visited = {}

    while open_list:
        f, current, g, parent = heapq.heappop(open_list)
        if current in visited:
            continue

        visited[current] = (g, parent)

        if current == goal:
            path = []
            while current:
                path.append(current)
                _, parent = visited[current]
                current = parent
            path.reverse()
            return path, visited[goal][0]

        for neighbor in graph[current]["neighbors"]:
            if neighbor in visited:
                continue
            g_new = g + haversine_distance(graph[current], graph[neighbor])
            h = haversine_distance(graph[neighbor], graph[goal])
            f_new = g_new + h
            heapq.heappush(open_list, (f_new, neighbor, g_new, current))

    return None, float("inf")
