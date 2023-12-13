import math
import random

def monte_carlo_sine_area(n):
    points_below_curve = 0

    for _ in range(n):
        x = random.uniform(0, math.pi)
        y = random.uniform(0, 1)
        if y <= math.sin(x):
            points_below_curve += 1

    area_ratio = points_below_curve / n
    total_area = math.pi

    estimated_area = total_area * area_ratio
    return estimated_area

num_points = int(input("Digite a quantidade de pontos para a estimativa da área da função seno: "))

result = monte_carlo_sine_area(num_points)
print(f"Estimativa da área da função seno: {result}")

