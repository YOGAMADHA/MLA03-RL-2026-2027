V = {"A": 0, "B": 0, "C": 0, "Goal": 0}

cost = {"A": 4, "B": 3, "C": 1}

for _ in range(10):
    V["C"] = cost["C"] + V["Goal"]
    V["B"] = cost["B"] + V["C"]
    V["A"] = cost["A"] + V["B"]

print("Minimum Travel Cost:", V["A"])
