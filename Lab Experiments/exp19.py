import random

robots = ["Robot1", "Robot2", "Robot3"]
tasks = ["Pick", "Pack", "Deliver"]

for robot in robots:
    task = random.choice(tasks)
    print(robot, "->", task)

print("Multi-Agent Task Allocation Completed.")
