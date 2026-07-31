import random

observations = ["Clear", "Obstacle", "Victim"]

for _ in range(5):
    observation = random.choice(observations)

    if observation == "Victim":
        action = "Rescue"
    elif observation == "Obstacle":
        action = "Turn"
    else:
        action = "Move"

    print("Observation:", observation, "Action:", action)

print("POMDP Search and Rescue Completed.")
