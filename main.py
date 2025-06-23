import tkinter as tk
from tkinter import ttk, messagebox
from cities import graph
from utils import a_star
from map_utils import plot_route
import webbrowser
import os

def find_path():
    start = start_var.get()
    goal = goal_var.get()

    if start == goal:
        messagebox.showinfo("Info", "Start and Goal are the same.")
        return

    if start not in graph or goal not in graph:
        messagebox.showerror("Error", "Invalid city selected.")
        return

    path, cost = a_star(start, goal)
    if path:
        result = f"✅ Shortest Path:\n{' → '.join(path)}\n\n📏 Distance: {cost:.2f} km"

        # Generate and open folium map
        map_file = plot_route(path)
        if os.path.exists(map_file):
            webbrowser.open(f"file://{os.path.abspath(map_file)}")
    else:
        result = "❌ No path found."

    result_label.config(text=result)

# --- GUI Setup ---
root = tk.Tk()
root.title("🗺️ Geospatial City Navigator (A* Pathfinding)")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

city_list = sorted(graph.keys())

tk.Label(root, text="A* Path Finder using Geospatial Data", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack()

start_var = tk.StringVar()
goal_var = tk.StringVar()

ttk.Label(frame, text="Start City:").grid(row=0, column=0, padx=5, pady=5)
ttk.Combobox(frame, textvariable=start_var, values=city_list, width=30, state="readonly").grid(row=0, column=1)

ttk.Label(frame, text="Goal City:").grid(row=1, column=0, padx=5, pady=5)
ttk.Combobox(frame, textvariable=goal_var, values=city_list, width=30, state="readonly").grid(row=1, column=1)

tk.Button(root, text="Find Shortest Path", command=find_path, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="white", fg="#333", wraplength=500, justify="left")
result_label.pack(padx=20, pady=10, fill="both")

root.mainloop()
