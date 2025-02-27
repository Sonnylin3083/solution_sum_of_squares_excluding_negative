def main():
    # Read the number of test cases
    n = int(input())
    
    # Process each test case recursively
    results = process_test_cases(n, [])
    
    # Print all results
    print_results(results, 0)

def process_test_cases(remaining_cases, results):
    if remaining_cases == 0:
        return results
    
    # Read number of integers in this test case
    x = int(input())
    
    # Read space-separated integers
    values = list(map(int, input().split()))
    
    # Use only the first x integers
    values = values[:x]
    
    # Calculate sum of squares (excluding negatives)
    sum_squares = sum_squares_recursive(values, 0, 0)
    
    # Add to results list
    return process_test_cases(remaining_cases - 1, results + [sum_squares])

def sum_squares_recursive(values, index, total):
    if index >= len(values):
        return total
    
    # Only add to total if the current value is non-negative
    current_value = values[index]
    increment = current_value ** 2 if current_value >= 0 else 0
    
    return sum_squares_recursive(values, index + 1, total + increment)

def print_results(results, index):
    if index >= len(results):
        return
    
    print(results[index])
    print_results(results, index + 1)

if __name__ == "__main__":
    main()