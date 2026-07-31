import random

actions = ["Walk", "Left", "Right", "Stop"]
policy = {a: 0 for a in actions}

for _ in range(100):
    action = random.choice(actions)
    reward = 1 if action == "Walk" else -1
    policy[action] += reward

print("PPO/TRPO Policy:", policy)
print("Best Action:", max(policy, key=policy.get))
