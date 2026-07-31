import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(16, activation="relu", input_shape=(4,)),
    Dense(16, activation="relu"),
    Dense(2)
])

model.compile(optimizer="adam", loss="mse")

state = np.random.rand(1, 4)
q_values = model.predict(state, verbose=0)

print("Drone Q-Values:", q_values)
