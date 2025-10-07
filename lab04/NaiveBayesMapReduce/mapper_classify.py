import math, sys

model = {}
class_counts = {}
total_samples = 0

with open('output.txt', 'r') as f:
    for line in f:
        key, value = line.strip().split('\t')
        value = int(value)
        key = key.strip('()')
        parts = key.split(',')
        
        if parts[0] == 'play':
            class_counts[parts[1]] = value
            total_samples += value
        else:
            model[(parts[0], parts[1], parts[2])] = value

# Laplace smoothing
def cond_prob(feature, fval, label):
    count = model.get((feature, fval, label), 0)
    total_label = class_counts[label]
    return (count + 1) / (total_label + len({f for (f, _, _) in model if f == feature}))

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    values = {'outlook': parts[0], 'temp': parts[1], 'humidity': parts[2], 'wind': parts[3]}

    for label in class_counts:
        prior = class_counts[label] / total_samples
        prop_log = math.log(prior)
        for feat in values:
            prop_log += math.log(cond_prob(feat, values[feat], label))
        print(f"{line}\t{label}\t{prop_log}")   