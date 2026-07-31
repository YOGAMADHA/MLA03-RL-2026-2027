import random

actions = ["Left", "Straight", "Right"]
score = {a: 0 for a in actions}

for _ in range(100):
    action = random.choice(actions)
    reward = 5 if action == "Straight" else -1
    score[action] += reward

print("Lane Keeping Policy:", score)
