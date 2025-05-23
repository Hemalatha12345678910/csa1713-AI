import math

# Sample dataset: [feature1, feature2, ..., label]
dataset = [
    [2.7, 2.5, 'A'],
    [1.3, 1.5, 'A'],
    [3.0, 4.0, 'B'],
    [5.0, 6.0, 'B'],
    [1.0, 1.0, 'A'],
    [6.0, 5.5, 'B']
]

def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    ent = 0.0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

def split_dataset(data, feature_index, threshold):
    left = [row for row in data if row[feature_index] <= threshold]
    right = [row for row in data if row[feature_index] > threshold]
    return left, right

def information_gain(data, feature_index, threshold):
    parent_entropy = entropy(data)
    left, right = split_dataset(data, feature_index, threshold)
    if not left or not right:
        return 0
    n = len(data)
    n_left, n_right = len(left), len(right)
    child_entropy = (n_left / n) * entropy(left) + (n_right / n) * entropy(right)
    return parent_entropy - child_entropy

def majority_class(data):
    counts = {}
    for row in data:
        label = row[-1]
        counts[label] = counts.get(label, 0) + 1
    return max(counts, key=counts.get)

class Node:
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, *, value=None):
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value  # for leaf nodes

def build_tree(data, depth=0, max_depth=3):
    labels = [row[-1] for row in data]
    if len(set(labels)) == 1:
        return Node(value=labels[0])  # Pure leaf

    if depth >= max_depth:
        return Node(value=majority_class(data))  # Max depth reached

    best_gain = 0
    best_feature, best_threshold = None, None
    n_features = len(data[0]) - 1

    for feature_index in range(n_features):
        values = set(row[feature_index] for row in data)
        for threshold in values:
            gain = information_gain(data, feature_index, threshold)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature_index
                best_threshold = threshold

    if best_gain == 0:
        return Node(value=majority_class(data))

    left_data, right_data = split_dataset(data, best_feature, best_threshold)
    left_child = build_tree(left_data, depth + 1, max_depth)
    right_child = build_tree(right_data, depth + 1, max_depth)
    return Node(best_feature, best_threshold, left_child, right_child)

def predict(node, sample):
    if node.value is not None:
        return node.value
    if sample[node.feature_index] <= node.threshold:
        return predict(node.left, sample)
    else:
        return predict(node.right, sample)

# Build the tree
tree = build_tree(dataset)

# Test prediction
test_sample = [3.5, 4.5]
predicted_class = predict(tree, test_sample)
print(f"Predicted class for {test_sample} is '{predicted_class}'")
