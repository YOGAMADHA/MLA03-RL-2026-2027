states = ["Start", "Shelf", "Packing", "Goal"]

actions = {
    "Start": "Move",
    "Shelf": "Pick",
    "Packing": "Pack"
}

rewards = {
    "Start": -1,
    "Shelf": 5,
    "Packing": 5,
    "Goal": 10
}

for state in states:
    print(state, "->", rewards[state])

print("Optimal Path:", "Start -> Shelf -> Packing -> Goal")
