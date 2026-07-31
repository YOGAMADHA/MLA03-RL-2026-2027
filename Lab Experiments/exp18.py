import random

tasks = ["Welding", "Painting", "Assembly"]
learning = {task: 0 for task in tasks}

for _ in range(100):
    task = random.choice(tasks)
    learning[task] += random.choice([0, 1])

print("Meta-RL Learning:", learning)
