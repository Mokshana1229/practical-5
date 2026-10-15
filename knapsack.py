def knapsack_recursive(W, weights, values, n):
    if n == 0 or W == 0:
        return 0

    if weights[n-1] > W:
        return knapsack_recursive(W, weights, values, n-1)
  
    include = values[n-1] + knapsack_recursive(W - weights[n-1], weights, values, n-1)
    exclude = knapsack_recursive(W, weights, values, n-1)
    
    return max(include, exclude)

values = [50, 100, 150, 200]
weights = [8, 16, 32, 10]
capacity = 64
n = len(values)

result = knapsack_recursive(capacity, weights, values, n)
print(f"Maximum value (Recursive): {result}")
