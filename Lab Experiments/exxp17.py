tasks = {
    "Cleaning": ["Move", "Pick", "Clean"],
    "Cooking": ["Move", "Pick", "Cook"]
}

for task, actions in tasks.items():
    print(task, ":", " -> ".join(actions))

print("Household tasks completed.")
