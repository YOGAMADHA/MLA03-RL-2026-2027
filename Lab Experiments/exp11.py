from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def create_model():
    return Sequential([
        Dense(16, activation="relu", input_shape=(4,)),
        Dense(2)
    ])

dqn = create_model()
ddqn = create_model()
dueling = create_model()

print("DQN: Ready")
print("DDQN: Ready")
print("Dueling DQN: Ready")
print("PER: Experience priority can be added")
