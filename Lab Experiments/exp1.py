# MDP for a Simplified Chess Game
# Using Value Iteration

import random

# States represent the position of the agent's king and opponent's king
states = [
    "Start",
    "Move1",
    "Move2",
    "Attack",
    "Win",
    "Lose"
]

# Possible actions for each state
actions = {
    "Start": ["Move_Forward", "Move_Side"],
    "Move1": ["Move_Forward", "Attack"],
    "Move2": ["Attack", "Move_Side"],
    "Attack": ["Capture"],
    "Win": [],
    "Lose": []
}

# Transition probabilities
# Each action leads to a new state with a probability
transitions = {
    ("Start", "Move_Forward"): [("Move1", 0.8), ("Lose", 0.2)],
    ("Start", "Move_Side"): [("Move2", 0.7), ("Lose", 0.3)],

    ("Move1", "Move_Forward"): [("Move2", 0.8), ("Lose", 0.2)],
    ("Move1", "Attack"): [("Win", 0.7), ("Lose", 0.3)],

    ("Move2", "Attack"): [("Win", 0.9), ("Lose", 0.1)],
    ("Move2", "Move_Side"): [("Move1", 0.6), ("Lose", 0.4)],

    ("Attack", "Capture"): [("Win", 1.0)]
}

# Reward function
rewards = {
    "Win": 100,
    "Lose": -100,
    "Move1": -1,
    "Move2": -1,
    "Attack": 10,
    "Start": 0
}

# Value Iteration parameters
gamma = 0.9
V = {state: 0 for state in states}

# Value Iteration
for iteration in range(100):
    new_V = V.copy()

    for state in states:

        if state in ["Win", "Lose"]:
            continue

        if not actions[state]:
            continue

        values = []

        for action in actions[state]:

            value = 0

            for next_state, probability in transitions[(state, action)]:
                value += probability * (
                    rewards[next_state] + gamma * V[next_state]
                )

            values.append(value)

        new_V[state] = max(values)

    V = new_V

# Display state values
print("State Values:")
for state in states:
    print(state, ":", round(V[state], 2))

# Find optimal action for each state
policy = {}

for state in states:

    if not actions[state]:
        continue

    best_action = None
    best_value = float("-inf")

    for action in actions[state]:

        value = 0

        for next_state, probability in transitions[(state, action)]:
            value += probability * (
                rewards[next_state] + gamma * V[next_state]
            )

        if value > best_value:
            best_value = value
            best_action = action

    policy[state] = best_action

# Display optimal policy
print("\nOptimal Policy:")
for state, action in policy.items():
    print(state, "->", action)

# Generate optimal sequence
print("\nOptimal Sequence:")

current_state = "Start"

while current_state not in ["Win", "Lose"]:

    action = policy[current_state]

    print("State:", current_state, "| Action:", action)

    possible_states = transitions[(current_state, action)]

    # Select state with highest transition probability
    next_state = max(possible_states, key=lambda x: x[1])[0]

    current_state = next_state

print("Final State:", current_state)

if current_state == "Win":
    print("Result: Agent wins the simplified chess game!")
else:
    print("Result: Agent loses the game.")
