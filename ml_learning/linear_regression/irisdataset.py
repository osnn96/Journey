from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Display the feature data
print("Features (data):")
print(iris.data)

# Display the target labels
print("\nTarget (labels):")
print(iris.target)


# Print feature names
print("\nFeature Names:")
print(iris.feature_names)

# Print target names
print("\nTarget Names:")
print(iris.target_names)
