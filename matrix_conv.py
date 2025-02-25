import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

def update_matrix(M):
    """
    Given a binary matrix M, slide a 3x3 window over it,
    compute the sum of the eight neighbors (excluding the center),
    and flip the center cell if that sum is odd.
    """
    # 3x3 kernel that sums up all cells except the center.
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    # Use convolution. Here, we assume that out-of-bound cells are 0.
    neighbors_sum = convolve2d(M, kernel, mode='same', boundary='fill', fillvalue=0)
    # Create new matrix: if the sum of neighbors is odd, flip the cell; otherwise keep it.
    new_M = np.where(neighbors_sum % 2 == 1, 1 - M, M)
    return new_M

def main():
    # Accept matrix size from the user.
    N = int(input("Enter the size N of the NxN matrix: "))
    
    # Create an initial random binary matrix.
    M = np.random.randint(0, 2, (N, N))
    initial_M = M.copy()  # Keep a copy of the initial state.

    step = 0

    # Visualize the initial state.
    plt.figure(figsize=(5, 5))
    sns.heatmap(M, cbar=False, cmap='viridis', square=True, annot=True, fmt='d')
    plt.title(f"Step {step} (Initial)")
    plt.show()

    while True:
        new_M = update_matrix(M)
        step += 1
        
        # Plot the new matrix configuration.
        plt.figure(figsize=(5, 5))
        sns.heatmap(new_M, cbar=False, cmap='viridis', square=True, annot=True, fmt='d')
        plt.title(f"Step {step}")
        plt.show()
        5
        # Stop if the matrix has stabilized (no change) or if it returned to the initial configuration.
        if np.array_equal(new_M, M):
            print(f"Matrix converged at step {step}.")
            break
        if np.array_equal(new_M, initial_M):
            print(f"Matrix returned to the initial state at step {step}.")
            break
        
        # Update M for the next iteration.
        M = new_M.copy()

if __name__ == "__main__":
    main()
