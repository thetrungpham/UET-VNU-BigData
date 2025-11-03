#!/usr/bin/env python3
import sys

target_variable = 0             
continuous_variables = [1, 2, 3, 4]  

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    features = line.split()
    
    if len(features) <= max(continuous_variables):
        continue
    
    class_label = features[target_variable]


    for i in continuous_variables:
        try:
            val = float(features[i])
            print(f"{i}_{class_label}\t{val}")
        except ValueError:
            continue

    print(f"{target_variable}_{class_label}\t1.0")

    print(f"{target_variable}\t1.0")
