#!/usr/bin/env python3
import sys
from collections import defaultdict


feature_sums = defaultdict(float)      
feature_sqsums = defaultdict(float)     
feature_counts = defaultdict(int)      

class_counts = defaultdict(int)         
total_samples = 0                       

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")
    if len(parts) != 2:
        continue
    key, value = parts
    value = float(value)

    # Nếu key là '0' → tổng số mẫu
    if key == "0":
        total_samples += int(value)
    # Nếu key là class count → key = "targetVariable_classLabel"
    elif key.startswith("0_"):
        class_label = key.split("_")[1]
        class_counts[class_label] += int(value)
    # Nếu key là feature continuous → key = featureIndex_classLabel
    else:
        feature_sums[key] += value
        feature_sqsums[key] += value * value
        feature_counts[key] += 1

# Output kết quả Gaussian Naive Bayes
print("# Class probabilities P(C):")
for cls, count in class_counts.items():
    P_c = count / total_samples
    print(f"{cls}\t{P_c:.6f}")

print("\n# Feature statistics per class (mean, variance):")
for key in sorted(feature_sums.keys()):
    count = feature_counts[key]
    mean = feature_sums[key] / count
    variance = (feature_sqsums[key] / count) - (mean ** 2)
    print(f"{key}\tmean={mean:.6f}\tvariance={variance:.6f}")
