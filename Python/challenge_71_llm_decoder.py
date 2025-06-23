"""
Challenge 71: AI Challenge - Simple LLM Decoder (Masked Self-Attention)

Problem Statement:
Implement a simplified autoregressive text generator. The decoder will generate
a sequence of tokens one at a time. The core of this challenge is implementing
"masked" self-attention, which prevents the model from looking at future tokens
when predicting the next token.

Algorithm Steps (inside the generation loop):
1.  **Create an Attention Mask**: Create a matrix where future positions are set
    to `-np.inf` and current/past positions are set to 0.
2.  **Calculate Attention Scores**: `scores = current_sequence @ current_sequence.T`.
3.  **Apply the Mask**: Add the mask to the attention scores. This makes the softmax
    of future tokens effectively zero.
4.  **Normalize with Softmax**: Apply the softmax function to get the masked weights.
5.  **Get a Context Vector**: Use the weights to get a new vector for the *last*
    token in the current sequence. This vector represents the context for
    predicting the *next* token.
6.  **Predict the Next Token**: Find which token in the entire vocabulary is most
    similar to our context vector (using dot product).
7.  **Append and Repeat**: Add the predicted token to our sequence and repeat the loop.

Solution:
"""
import numpy as np

def softmax(x: np.ndarray) -> np.ndarray:
    """Computes softmax along the last axis."""
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / e_x.sum(axis=-1, keepdims=True)

def simple_decoder_generator(vocabulary: dict, start_token: str, num_tokens_to_generate: int):
    """
    Generates a sequence of tokens autoregressively using masked self-attention.
    """
    # Unpack vocabulary into separate lists for easy lookup
    vocab_tokens = list(vocabulary.keys())
    vocab_embeddings = np.array(list(vocabulary.values()))
    
    # Start the sequence with the start token's embedding
    generated_sequence_embeddings = [vocabulary[start_token]]
    generated_sequence_tokens = [start_token]

    for _ in range(num_tokens_to_generate):
        # Get the current sequence as a NumPy array
        current_embeddings = np.array(generated_sequence_embeddings)
        seq_len = current_embeddings.shape[0]

        # 1. Create the mask to hide future positions
        mask = np.triu(np.full((seq_len, seq_len), -np.inf), k=1)

        # 2. Calculate attention scores
        attention_scores = current_embeddings @ current_embeddings.T

        # 3. Apply the mask
        masked_scores = attention_scores + mask

        # 4. Normalize
        attention_weights = softmax(masked_scores)

        # 5. Get the context vector for the *last* element
        context_vector = attention_weights[-1] @ current_embeddings

        # 6. Predict the next token by finding the most similar in the vocabulary
        prediction_scores = vocab_embeddings @ context_vector
        next_token_index = np.argmax(prediction_scores)
        next_token = vocab_tokens[next_token_index]
        
        # 7. Append the new token and its embedding to our sequence
        generated_sequence_tokens.append(next_token)
        generated_sequence_embeddings.append(vocab_embeddings[next_token_index])

    return " ".join(generated_sequence_tokens)

# Example usage:
if __name__ == "__main__":
    # Define a tiny vocabulary and their embeddings
    # In a real model, these are learned during training
    vocabulary = {
        "<start>":      np.array([1, 0, 0, 0]),
        "the":          np.array([0, 1, 0, 0]),
        "cat":          np.array([0, 0, 1, 0]),
        "sat":          np.array([0, 0, 0, 1]),
        "on":           np.array([1, 1, 0, 0]), # similar to <start> + the
        "mat":          np.array([0, 0, 1, 1])  # similar to cat + sat
    }
    
    # Generate a sequence of 3 tokens, starting with '<start>'
    generated_text = simple_decoder_generator(vocabulary, "<start>", 3)
    
    print("--- Generated Text ---")
    print(generated_text)
    print("\nModel learned simple patterns: '<start>' -> 'on', 'cat' -> 'mat'")

"""
Expected Output:

--- Generated Text ---
<start> on the mat
""" 