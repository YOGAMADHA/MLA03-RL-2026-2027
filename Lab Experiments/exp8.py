import random

returns = []

for _ in range(100):
    reward = 10 if random.random() > 0.2 else -1
    returns.append(reward)

print("Monte Carlo Value:", sum(returns) / len(returns))
