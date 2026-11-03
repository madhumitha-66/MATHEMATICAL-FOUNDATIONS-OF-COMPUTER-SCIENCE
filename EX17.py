graph = {
    "Mathematics": ["Programming", "Networks"],
    "Programming": ["Mathematics", "Networks", "Database"],
    "Networks": ["Mathematics", "Programming", "Database"],
    "Database": ["Programming", "Networks"]
}

colors = {}

for subject in graph:
    used_colors = {
        colors[neighbour]
        for neighbour in graph[subject]
        if neighbour in colors
    }

    color = 1

    while color in used_colors:
        color += 1

    colors[subject] = color

print("EXAMINATION TIMETABLE")
print("---------------------")

for subject, color in colors.items():
    print(subject, "-> Slot", color)

print("\nTotal Slots Required:", max(colors.values()))
