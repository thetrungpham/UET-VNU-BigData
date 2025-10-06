import sys, math, json

centroids = json.loads(sys.argv[1])  # đọc các tâm cụm truyền từ driver

for line in sys.stdin:
    x, y = map(float, line.strip().split(','))
    min_dist = float('inf')
    nearest = None
    for i, (cx, cy) in enumerate(centroids):
        dist = math.sqrt((x - cx)**2 + (y - cy)**2)
        if dist < min_dist:
            min_dist, nearest = dist, i
    print(f"{nearest}\t{x},{y}")
