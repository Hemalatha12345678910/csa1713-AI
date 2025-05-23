import numpy as np
print(np.__version__)
# Activation function: sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input data (XOR)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Output labels
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Set seed for reproducibility
np.random.seed(0)

# Network architecture
input_layer_size = 2
hidden_layer_size = 4
output_layer_size = 1
learning_rate = 0.1
epochs = 10000

# Weight and bias initialization
W1 = np.random.randn(input_layer_size, hidden_layer_size)
b1 = np.zeros((1, hidden_layer_size))
W2 = np.random.randn(hidden_layer_size, output_layer_size)
b2 = np.zeros((1, output_layer_size))

# Training loop
for epoch in range(epochs):
    # Forward pass
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)

    # Loss (mean squared error)
    loss = np.mean((y - a2) ** 2)

    # Backward pass
    d2 = (y - a2) * sigmoid_derivative(a2)
    d1 = np.dot(d2, W2.T) * sigmoid_derivative(a1)

    # Update weights and biases
    W2 += np.dot(a1.T, d2) * learning_rate
    b2 += np.sum(d2, axis=0, keepdims=True) * learning_rate
    W1 += np.dot(X.T, d1) * learning_rate
    b1 += np.sum(d1, axis=0, keepdims=True) * learning_rate

    # Print loss every 1000 epochs
    if epoch % 1000 == 0:
        print(f"Epoch {epoch} | Loss: {loss:.4f}")

# Final predictions
print("\nFinal Predictions:")
print(np.round(a2, 3))

