import sys
import math

centroids = [(6, 9), (8, 6), (4, 8), (3,4)] 

for line in sys.stdin:
    parts = line.strip().split(',')
    points, x, y = str(parts[0]), float(parts[1]), float(parts[2])

    nearset = None
    min_dist = float('inf')
    
    for i, (cx, cy) in enumerate(centroids):
        dist = math.sqrt((x -cx)**2 + (y - cy)**2)
        if dist < min_dist:
            min_dist, nearset = dist, i
    print(f"{nearset} {x},{y}")