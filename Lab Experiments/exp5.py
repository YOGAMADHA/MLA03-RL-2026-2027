import random

Q = [0, 0, 0]
count = [0, 0, 0]
epsilon = 0.1

for _ in range(100):
    if random.random() < epsilon:
        ad = random.randint(0, 2)
    else:
        ad = Q.index(max(Q))

    reward = random.choice([0, 1])
    count[ad] += 1
    Q[ad] += (reward - Q[ad]) / count[ad]

print("Advertisement Values:", Q)
print("Best Advertisement:", Q.index(max(Q)) + 1)
