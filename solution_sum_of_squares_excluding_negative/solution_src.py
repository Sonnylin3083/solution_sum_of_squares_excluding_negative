def main():
	# read the number of test cases
    n = int(input())
    
    # process each test case recursively
    results = process_test_cases(n, [])
    
    # print all results
    print_results(results, 0)

def process_test_cases(remaining_cases, results):
    # check if still test cases remain
    if remaining_cases == 0:
        return results
    
    # read number of integers in this test case
    x = int(input())
    
    # read space-separated integers
    values = list(map(int, input().split()))
    
    # use only the first x integers
    values = values[:x]
    
    # calculate sum of squares (excluding negatives)
    sum_squares = sum_squares_recursive(values, 0, 0)
    
    # add to results list
    return process_test_cases(remaining_cases - 1, results + [sum_squares])

def sum_squares_recursive(values, index, total):
    # check if all values are computed
    if index >= len(values):
        return total
    
    # get the current value
    current_value = values[index]
    
    # only add to total if the current value is non-negative
    increment = current_value ** 2 if current_value >= 0 else 0
    
    return sum_squares_recursive(values, index + 1, total + increment)

def print_results(results, index):
    # check if any result is not printed yet
    if index >= len(results):
        return
    
    # print result of a test case
    print(results[index])
    
    # print the next result if there is
    print_results(results, index + 1)

if __name__ == "__main__":
    main()