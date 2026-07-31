import gymnasium as gym
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

env = gym.make("CartPole-v1")

model = Sequential([
    Dense(16, activation="relu", input_shape=(4,)),
    Dense(2)
])

model.compile(optimizer="adam", loss="mse")

state, _ = env.reset()

print("Robot Navigation Started")
print("State:", state)

env.close()
