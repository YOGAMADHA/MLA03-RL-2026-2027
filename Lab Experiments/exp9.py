import random

Q = [0, 0]

for _ in range(100):
    action = random.randint(0, 1)
    reward = random.choice([-1, 10])

    Q[action] += 0.1 * (reward - Q[action])

print("TD/SARSA/Q-Learning Values:", Q)
