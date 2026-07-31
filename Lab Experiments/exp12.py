import random

actions = ["Left", "Right", "Up", "Down"]
scores = {a: 0 for a in actions}

for _ in range(100):
    action = random.choice(actions)
    reward = 1 if action == "Right" else -1
    scores[action] += reward

print("Learned Policy:", scores)
print("Best Action:", max(scores, key=scores.get))
