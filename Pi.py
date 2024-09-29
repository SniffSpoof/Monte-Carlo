import random
import math

def estimate_pi(num_points):
    inside_circle = 0  # Count of points inside the circle

    # Generate points and check if they fall inside the unit circle
    for _ in range(num_points):
        x = random.uniform(0, 1)  # Generate a random x coordinate
        y = random.uniform(0, 1)  # Generate a random y coordinate
        distance = math.sqrt(x**2 + y**2)  # Calculate the distance from the origin

        if distance <= 1:  # Check if the point is inside the circle
            inside_circle += 1

    # Estimate the value of pi
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate

def main():
    num_points = int(input("Enter the number of points to generate: "))  # User input for number of points
    pi_estimate = estimate_pi(num_points)  # Estimate pi using the Monte Carlo method

    # Calculate the relative error
    relative_error = abs((math.pi - pi_estimate) / math.pi)

    # Output the results
    print(f"Estimated value of π: {pi_estimate}")
    print(f"Relative error: {relative_error:.6f}")

if __name__ == "__main__":
    main()

