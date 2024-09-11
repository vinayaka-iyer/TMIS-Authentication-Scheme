import hashlib
import numpy as np

# Chaotic map for generating chaotic sequences


def chebyshev_map(x, k):
    return np.cos(k * np.arccos(x))

# Chaotic hash function using Chebyshev map


def chaotic_hash(data: str, iterations: int = 100) -> str:
    x = 0.5  # Initial condition
    k = 3    # Chaotic map parameter
    for _ in range(iterations):
        x = chebyshev_map(x, k)
    # Hashing the data with the chaotic value
    return hashlib.sha256(str(data).encode() + str(x).encode()).hexdigest()
