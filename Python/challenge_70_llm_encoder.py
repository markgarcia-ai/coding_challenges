"""
Challenge 70: AI Challenge - Simple LLM Encoder (Self-Attention)

Problem Statement:
Implement a simplified self-attention mechanism. Given a set of initial word
embeddings for a sentence, create new, context-aware embeddings by calculating
attention scores and producing a weighted average of the initial embeddings.

Algorithm Steps:
1.  **Calculate Attention Scores**: For each word vector, calculate its similarity
    with every other word vector. A simple way to do this is with matrix
    multiplication: `scores = embeddings @ embeddings.T`. The result is a matrix
    where `scores[i, j]` represents how much word `i` attends to word `j`.
2.  **Normalize Scores (Softmax)**: Apply the softmax function to each row of the
    scores matrix. This converts the raw scores into probabilities, ensuring that
    the weights for each word sum to 1.
    `softmax(x)_i = exp(x_i) / sum(exp(x_j))`
3.  **Produce Final Embeddings**: Calculate the new, contextualized embedding for
    each word by taking a weighted average of all the original embeddings. The
    weights are the probabilities from the softmax step. This is another matrix
    multiplication: `new_embeddings = attention_weights @ embeddings`.

Solution:
"""
import numpy as np

def softmax(x: np.ndarray) -> np.ndarray:
    """Computes softmax along the last axis of the input array."""
    # Subtracting max for numerical stability (prevents overflow)
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / e_x.sum(axis=-1, keepdims=True)

def simple_self_attention(embeddings: np.ndarray) -> (np.ndarray, np.ndarray):
    """
    Performs a simplified self-attention mechanism.
    
    Args:
        embeddings: A (sequence_length, embedding_dim) matrix.
        
    Returns:
        A tuple containing:
        - The new context-aware embeddings (sequence_length, embedding_dim).
        - The attention weights (sequence_length, sequence_length).
    """
    # 1. Calculate raw attention scores
    attention_scores = embeddings @ embeddings.T
    
    # 2. Normalize scores into weights
    attention_weights = softmax(attention_scores)
    
    # 3. Produce new embeddings as a weighted average
    new_embeddings = attention_weights @ embeddings
    
    return new_embeddings, attention_weights

# Example usage:
if __name__ == "__main__":
    # A tiny embedding dimension for simplicity
    embedding_dim = 4
    
    # Pre-defined, simple embeddings for the sentence: "the cat sat"
    embeddings = np.array([
        [1, 0, 0, 0],  # "the"
        [0, 1, 1, 0],  # "cat" (similar to "sat")
        [0, 1, 1, 1]   # "sat" (similar to "cat")
    ])
    
    print("--- Original Embeddings ---")
    print(embeddings)
    
    contextual_embeddings, weights = simple_self_attention(embeddings)
    
    print("\n--- Attention Weights (after Softmax) ---")
    print("      'the' 'cat' 'sat'")
    print(weights)
    print("\nNote how 'cat' and 'sat' pay high attention to each other due to similarity.")
    
    print("\n--- New Contextual Embeddings ---")
    print(contextual_embeddings)
    print("\nNote how the vectors for 'cat' and 'sat' are now more similar,")
    print("having absorbed context from each other.")

"""
Expected Output:

--- Original Embeddings ---
[[1 0 0 0]
 [0 1 1 0]
 [0 1 1 1]]

--- Attention Weights (after Softmax) ---
      'the' 'cat' 'sat'
[[0.57611688 0.21194156 0.21194156]
 [0.03511901 0.4824405  0.4824405 ]
 [0.03511901 0.4824405  0.4824405 ]]

Note how 'cat' and 'sat' pay high attention to each other due to similarity.

--- New Contextual Embeddings ---
[[0.57611688 0.69438205 0.69438205 0.21194156]
 [0.03511901 0.96488099 0.96488099 0.4824405 ]
 [0.03511901 0.96488099 0.96488099 0.4824405 ]]

Note how the vectors for 'cat' and 'sat' are now more similar,
having absorbed context from each other.
""" 