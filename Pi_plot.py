import random
import math
import matplotlib.pyplot as plt

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate

def run_estimations(points_list):
    pi_estimates = []
    relative_errors = []

    for num_points in points_list:
        pi_estimate = estimate_pi(num_points)
        pi_estimates.append(pi_estimate)

        relative_error = abs((math.pi - pi_estimate) / math.pi)
        relative_errors.append(relative_error)

    plt.figure(figsize=(14, 6))

    # Plot for pi estimates
    plt.subplot(1, 2, 1)
    plt.plot(points_list, pi_estimates, marker='o', color='blue', label='Estimated π')
    plt.axhline(y=math.pi, color='red', linestyle='--', label='Actual π')
    plt.title('Estimation of π vs Number of Points', fontsize=16)
    plt.xlabel('Number of Points', fontsize=14)
    plt.ylabel('Estimated Value of π', fontsize=14)
    plt.xscale('log')  # Log scale for better visualization
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Plot for relative errors
    plt.subplot(1, 2, 2)
    plt.plot(points_list, relative_errors, marker='o', color='green', label='Relative Error')
    plt.title('Relative Error vs Number of Points', fontsize=16)
    plt.xlabel('Number of Points', fontsize=14)
    plt.ylabel('Relative Error', fontsize=14)
    plt.xscale('log')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    plt.tight_layout()
    plt.show()


# List of different numbers of points to test
points_list = [1, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000]

# Run the estimations and generate plots
run_estimations(points_list)

