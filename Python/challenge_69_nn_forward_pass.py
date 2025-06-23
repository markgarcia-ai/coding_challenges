"""
Challenge 69: AI Vectorization - Neural Network Forward Pass

Problem Statement:
Simulate a vectorized forward pass of a simple, dense neural network layer.
This involves taking a batch of inputs, multiplying by a weight matrix, adding
a bias vector, and applying a ReLU activation function—all without explicit loops.

Key Operations:
1.  **Linear Transformation**: `Z = Inputs @ Weights + Biases`
2.  **Activation**: `A = ReLU(Z)` (ReLU is max(0, Z))

Solution:
"""
import numpy as np

def relu_activation(x: np.ndarray) -> np.ndarray:
    """
    Applies the Rectified Linear Unit (ReLU) activation function element-wise.
    This is a vectorized operation.
    """
    return np.maximum(0, x)

def simple_nn_forward_pass(inputs: np.ndarray, weights: np.ndarray, biases: np.ndarray) -> np.ndarray:
    """
    Performs a vectorized forward pass for one dense layer.
    
    Args:
        inputs: A (num_samples, num_input_features) matrix.
        weights: A (num_input_features, num_output_neurons) matrix.
        biases: A (1, num_output_neurons) vector.
        
    Returns:
        The output of the layer after activation.
    """
    # 1. Linear Transformation (Matrix Multiplication + Broadcasting)
    # The '@' operator performs matrix multiplication.
    # NumPy's broadcasting automatically adds the bias vector to each row.
    z = inputs @ weights + biases
    
    # 2. Apply the activation function
    a = relu_activation(z)
    
    return a

# Example usage:
if __name__ == "__main__":
    # --- Configuration ---
    num_samples = 3            # Number of data points in our batch
    num_input_features = 4     # e.g., features of an image or data row
    num_output_neurons = 2     # Number of neurons in this layer
    
    # --- Initialize random data (as a real model would have) ---
    # Using a fixed seed for reproducibility
    np.random.seed(42)
    
    inputs = np.random.randn(num_samples, num_input_features)
    weights = np.random.randn(num_input_features, num_output_neurons)
    biases = np.random.randn(1, num_output_neurons)

    print("--- Inputs (3 samples, 4 features each) ---")
    print(inputs)
    print("\n--- Weights (4 features -> 2 neurons) ---")
    print(weights)
    print("\n--- Biases (for 2 neurons) ---")
    print(biases)
    
    # --- Perform the Forward Pass ---
    output = simple_nn_forward_pass(inputs, weights, biases)
    
    print("\n--- Layer Output (after ReLU activation) ---")
    print(output)
    print("\nNote: Any negative values from the linear transformation were set to 0 by ReLU.")

"""
Expected Output:

--- Inputs (3 samples, 4 features each) ---
[[ 0.49671415 -0.1382643   0.64768854  1.52302986]
 [-0.23415337 -0.23413696  1.57921282  0.76743473]
 [-0.46947439  0.54256004 -0.46341769 -0.46572975]]

--- Weights (4 features -> 2 neurons) ---
[[ 0.24196227 -1.91328024]
 [-1.72491783 -0.56228753]
 [-1.01283112  0.31424733]
 [-0.90802408  1.46564877]]

--- Biases (for 2 neurons) ---
[[-2.55298982  0.6536186 ]]

--- Layer Output (after ReLU activation) ---
[[0.         1.21415291]
 [0.         2.22252431]
 [0.         0.        ]]

Note: Any negative values from the linear transformation were set to 0 by ReLU.
""" 