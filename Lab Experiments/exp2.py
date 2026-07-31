import random

states = ["Start", "Room1", "Room2", "Kitchen", "Goal"]
actions = ["Forward", "Left", "Right"]

Q = {s: {a: 0 for a in actions} for s in states}

rewards = {
    "Start": 0,
    "Room1": -1,
    "Room2": -1,
    "Kitchen": 5,
    "Goal": 10
}

for episode in range(500):
    state = "Start"

    while state != "Goal":
        if random.random() < 0.2:
            action = random.choice(actions)
        else:
            action = max(Q[state], key=Q[state].get)

        next_state = random.choice(["Room1", "Room2", "Kitchen"])
        reward = rewards[next_state]

        Q[state][action] += 0.1 * (
            reward + 0.9 * max(Q[next_state].values())
            - Q[state][action]
        )

        state = next_state

print("Learned Q-Values:")
for state in states:
    print(state, Q[state])
