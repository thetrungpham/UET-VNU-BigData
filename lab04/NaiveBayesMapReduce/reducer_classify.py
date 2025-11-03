import sys

current_instance = None
best_label = None
best_prob = -float("inf")

for line in sys.stdin:
    instance, label, log_prob = line.strip().split('\t')
    log_prob = float(log_prob)

    if current_instance == instance:
        if log_prob > best_prob:
            best_prob = log_prob
            best_label = label

    else:
        if current_instance:
            print(f"{current_instance}\t{best_label}\t{best_prob}")
        current_instance = instance
        best_label = label

if current_instance:
    print(f"{current_instance}\t{best_label}\t{best_prob}")