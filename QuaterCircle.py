import random

# Parameters
num_points = 10000
radius = 1.0

# Function to check if a point is inside the quarter circle
def is_inside_quarter_circle(x, y, radius):
    return x**2 + y**2 <= radius**2 and x >= 0 and y >= 0

# Monte Carlo simulation for area estimation of a quarter circle
def estimate_area_quarter_circle(num_points, radius):
    inside_points = 0
    for _ in range(num_points):
        x = random.uniform(0, radius)
        y = random.uniform(0, radius)
        if is_inside_quarter_circle(x, y, radius):
            inside_points += 1
    area_ratio = inside_points / num_points
    estimated_area = area_ratio * (radius**2)
    return estimated_area

# Estimate the area of the quarter circle
estimated_area = estimate_area_quarter_circle(num_points, radius)
print("Estimated area of the quarter circle:", estimated_area)
