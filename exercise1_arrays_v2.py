import numpy as np

data = np.array([
    [120, 150, 160, 180, 200, 215],
    [95, 105, 118, 135, 145, 155],
    [85, 92, 101, 115, 125, 135],
    [210, 220, 230, 245, 260, 275]
])
print("Array of transactions:\n", data)

branch_totals = data.sum(axis=1)
print("\nTotals for each branch:", branch_totals)

top_branch = np.argmax(branch_totals) + 1
print("\nBranch with largest total transactions:", top_branch)

overall_average = data.mean()
print("\nOverall average monthly volume:", overall_average)

reshaped_data = data.reshape(3, 8)
print("\nNew shape (3 x 8):\n", reshaped_data)
print("\nNote: Reshaping reorganizes the data layout but values remain unchanged.")
