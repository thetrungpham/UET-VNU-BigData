import sys

current_cluster = None
sum_x = sum_y = count = 0

for line in sys.stdin:
    cluster, point = line.strip().split(' ')
    x, y = map(float, point.split(','))

    if current_cluster is None:
        current_cluster = cluster

    if cluster != current_cluster:
        print(f"{sum_x/count} {sum_y/count}")
        sum_x = sum_y = count = 0
        current_cluster = cluster

    sum_x += x
    sum_y += y
    count += 1

if count > 0:
    print(f"{sum_x/count} {sum_y/count}")
