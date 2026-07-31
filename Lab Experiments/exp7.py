V = [0, 0, 0, 10]

cost = [
    [0, 2, 5, 0],
    [0, 0, 1, 4],
    [0, 0, 0, 2]
]

for _ in range(10):
    for s in range(3):
        values = [
            cost[s][n] + V[n]
            for n in range(4)
            if cost[s][n] > 0
        ]
        V[s] = min(values)

print("Optimal Taxi Cost:", V[0])
