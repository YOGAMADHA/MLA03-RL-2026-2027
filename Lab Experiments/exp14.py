import random

actions = ["Up", "Down", "Stop"]
value = {a: 0 for a in actions}

for _ in range(100):
    action = random.choice(actions)
    reward = random.choice([-1, 1, 5])
    value[action] += reward

print("Elevator Policy:", value)
print("Best Action:", max(value, key=value.get))
