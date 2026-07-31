import random

actions = ["Left", "Right", "Forward", "Stop"]
score = {a: 0 for a in actions}

for _ in range(100):
    action = random.choice(actions)
    reward = 10 if action == "Stop" else -1
    score[action] += reward

print("Parking Policy:", score)
print("Best Action:", max(score, key=score.get))
